// Cloudflare Pages Function: POST /api/contact
//
// Sends the contact form to the company mailbox via Resend
// (https://resend.com). No third-party SDK required — just a single fetch.
//
// Required environment variable (Cloudflare Pages → Settings → Environment variables):
//   RESEND_API_KEY          Resend API key (starts with "re_")
// Optional:
//   CONTACT_TO_EMAIL        Recipient address          (default: turbinevip@163.com)
//   CONTACT_FROM_EMAIL      Verified sender "from"     (default: onboarding@resend.dev — TEST ONLY)
//   CONTACT_SUBJECT_PREFIX  Subject prefix             (default: "[turbinevip.com]")
//
// NOTE: onboarding@resend.dev only delivers to your own Resend account email.
// For production, verify turbinevip.com in Resend and set
// CONTACT_FROM_EMAIL=no-reply@turbinevip.com (or another verified address).

const RESEND_ENDPOINT = "https://api.resend.com/emails";
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MAX_LENGTHS = { name: 120, email: 254, company: 200, product: 200, message: 5000 };

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // --- parse body (accept JSON or form-encoded) ---
  let body = {};
  try {
    const ct = request.headers.get("content-type") || "";
    if (ct.includes("application/json")) {
      body = await request.json();
    } else {
      const fd = await request.formData();
      for (const [k, v] of fd.entries()) body[k] = typeof v === "string" ? v : "";
    }
  } catch {
    return json({ ok: false, error: "Invalid request body." }, 400);
  }

  const name = String(body.name || "").trim();
  const email = String(body.email || "").trim();
  const company = String(body.company || "").trim();
  const product = String(body.product || "").trim();
  const message = String(body.message || "").trim();
  const website = String(body.website || "").trim(); // honeypot

  // Honeypot: real users never see/fill this hidden field. Bots do.
  // Pretend success so spam bots get no signal.
  if (website) {
    return json({ ok: true, message: "Thank you." });
  }

  // --- validation ---
  if (!name || name.length > MAX_LENGTHS.name) {
    return json({ ok: false, error: "Please enter a valid name." }, 400);
  }
  if (!email || email.length > MAX_LENGTHS.email || !EMAIL_RE.test(email)) {
    return json({ ok: false, error: "Please enter a valid email address." }, 400);
  }
  if (!message || message.length > MAX_LENGTHS.message) {
    return json({ ok: false, error: "Please enter a message." }, 400);
  }
  if (company.length > MAX_LENGTHS.company || product.length > MAX_LENGTHS.product) {
    return json({ ok: false, error: "Some fields are too long." }, 400);
  }

  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return json({ ok: false, error: "Server not configured (missing RESEND_API_KEY)." }, 500);
  }

  const toEmail = env.CONTACT_TO_EMAIL || "turbinevip@163.com";
  const fromEmail = env.CONTACT_FROM_EMAIL || "onboarding@resend.dev";
  const prefix = env.CONTACT_SUBJECT_PREFIX || "[turbinevip.com]";

  const text = [
    "New website inquiry",
    "",
    `Name: ${name}`,
    `Email: ${email}`,
    company ? `Company: ${company}` : "",
    product ? `Product/Service: ${product}` : "",
    "",
    "Message:",
    message,
  ].filter((l) => l !== "").join("\n");

  try {
    const res = await fetch(RESEND_ENDPOINT, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: `TurbineVIP Contact <${fromEmail}>`,
        to: [toEmail],
        reply_to: email,
        subject: `${prefix} New inquiry from ${name}`,
        text,
      }),
    });

    if (!res.ok) {
      return json({ ok: false, error: "Email service error, please try again." }, 502);
    }
    return json({ ok: true, message: "Thank you. Your message has been sent." });
  } catch {
    return json({ ok: false, error: "Failed to send email, please try again." }, 502);
  }
}
