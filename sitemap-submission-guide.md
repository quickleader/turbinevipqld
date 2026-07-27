# TurbineVip.com Sitemap 提交清单（Google Search Console + 百度站长平台）

> 本文档为**本地操作指引**，由 AI 整理、需您本人登录账号执行（AI 无法代登第三方账号）。
> 适用于 turbinevip.com 多语言站（en / zh / it）。

---

## 一、待提交的 Sitemap URL

| 类型 | URL | 包含 URL 数 |
|---|---|---|
| 根索引（推荐主提交） | `https://www.turbinevip.com/sitemap.xml` | 索引 3 个子 sitemap |
| 英文版 | `https://www.turbinevip.com/en/sitemap.xml` | 38 |
| 中文版 | `https://www.turbinevip.com/zh/sitemap.xml` | 37 |
| 意大利语版 | `https://www.turbinevip.com/it/sitemap.xml` | 37 |

**建议**：主提交根索引 `sitemap.xml`，Google/Baidu 会自动抓取下面 3 个子 sitemap。
如需加速各语言收录，可再分别提交 `en/zh/it` 三个子 sitemap。

---

## 二、Google Search Console（GSC）提交步骤

1. 登录 https://search.google.com/search-console/
2. 若未添加属性：点「添加资源」→ 选「网址前缀」输入 `https://www.turbinevip.com/` → 用 **HTML 标记 / 域名提供商 / DNS** 任一方式验证所有权。
3. 左侧菜单「索引」→「Sitemap」。
4. 在输入框填 `sitemap.xml`（只需填相对名，GSC 自动补全为 `https://www.turbinevip.com/sitemap.xml`）→ 点「提交」。
5. （可选）再分别提交 `en/sitemap.xml`、`zh/sitemap.xml`、`it/sitemap.xml`。
6. 提交后观察「状态」列：
   - 已发现 URL 数是否 = 预期（根索引约 112 条：38+37+37）；
   - 是否有「无法读取 / 含有错误」报错。

### GSC 多语言 / Geo 校验
- 本站在每个页面已输出 `hreflang`：`en` / `zh-cn` / `it` / `x-default`，且三语互链正确（已审计修复）。
- 在 GSC「URL 检查」中抽测几个 `zh/...` 页面，确认「国际定位」显示 `zh-cn`、且「引用的 hreflang」回链正常。
- 注：GSC 旧版「国际定位 / 地域定向」设置已弃用，现靠 hreflang 自动识别，无需手动设国家。

---

## 三、百度站长平台（搜索资源平台）提交步骤

1. 登录 https://ziyuan.baidu.com/ （百度搜索资源平台 / 站长平台）
2. 添加站点 `turbinevip.com` 并验证所有权（文件验证 / HTML 标签 / CNAME 解析，三选一）。
3. 进入「站点管理」→「数据提交」→「sitemap」。
4. 提交：
   - **主推中文版**：`https://www.turbinevip.com/zh/sitemap.xml`（百度对中国站点权重更相关）；
   - 同时可提交根索引：`https://www.turbinevip.com/sitemap.xml`。
5. 查看「sitemap 提交历史」状态（正常 / 处理中 / 失败及原因）。

### 百度 Geo 说明
- 百度默认面向中国用户，中文站无需额外地域设置；确保 `zh` 版内容为简体中文、`<html lang="zh-cn">`（本站点已配置）。
- 英文/意大利语页面在百度收录权重较低属正常现象，不影响中文站收录。

---

## 四、提交后验证（1–2 周内）

- **GSC**：「覆盖率」报告观察「有效 / 已编入索引」URL 是否增长；「URL 检查」抽测 `en/products/...`、`zh/products/...` 是否已编入索引。
- **百度**：「站点管理 → 数据提交 → sitemap」看已抓取 URL 数；「搜索展现」看曝光趋势。
- **手动抽查**：在 Google / 百度 分别搜 `site:turbinevip.com`，对比提交前后收录量。

---

## 五、已知小项（不影响提交，建议后续处理）

1. **sitemap `lastmod` 偏旧**：当前显示 `2026-07-03`（= git 末次提交日），非本次 7/24 构建日。原因：页面 frontmatter 未设 `lastmod`，Hugo 回退到 git 提交时间。
   - 影响：爬虫可能认为"页面未变更"而降低重抓频率，新内容收录略慢。
   - 修复方向（二选一）：
     - (a) 提交 git 后重建，使 lastmod 跟随最新提交；或
     - (b) 在 `hugo.toml` 的 sitemap 输出启用自动 lastmod（基于 `.Date` 或 git 历史），例如配置 `enableGitInfo = true` 并在 frontmatter 用 `{{ .GitInfo.AuthorDate }}` 类逻辑（需确认主题/模块支持）。
2. **本次已完成的站点改动**（WebP 全量替换、hreflang 去重修复、robots.txt 清理、移动端图标）均已构建进 `public/`，提交 sitemap 后爬虫即可拉取新页面。
3. **生产发布状态**：当前 `public/` 仅为本地构建 + CloudStudio 沙箱预览，**尚未推送到 turbinevip.com 真实服务器**。提交 sitemap 前请确认生产站已上线最新 `public/`，否则爬虫将抓到旧页面或 404。

---

## 六、前置检查（提交前务必确认）

- [ ] 生产服务器已部署最新 `public/`（非仅本地/沙箱）
- [ ] `https://www.turbinevip.com/sitemap.xml` 在公网可访问（返回 XML，非 404）
- [ ] robots.txt 含 `Sitemap: https://www.turbinevip.com/sitemap.xml`（本站点已配置）
- [ ] 三大语言版首页均可正常打开、无裂图（WebP 已生效）
