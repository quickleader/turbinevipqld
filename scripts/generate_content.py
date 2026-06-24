#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate multi-language product, FAQ, cases and certifications content for turbinevip-demo."""
import os
from pathlib import Path

BASE = Path("D:/wbwork/2026-06-24-17-36-06/turbinevip-demo")


def yml_str(value):
    """Return a YAML-safe double-quoted string, escaping internal double quotes."""
    text = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def make_frontmatter(fields):
    lines = ["---"]
    for key, value in fields.items():
        if key == "faq":
            lines.append("faq:")
            for item in value:
                lines.append(f"  - q: {yml_str(item['q'])}")
                lines.append(f"    a: {yml_str(item['a'])}")
        elif key == "certificates":
            lines.append("certificates:")
            for cert in value:
                lines.append("  - name: " + yml_str(cert["name"]))
                lines.append("    image: " + yml_str(cert["image"]))
                lines.append("    issuer: " + yml_str(cert["issuer"]))
                lines.append("    scope: " + yml_str(cert["scope"]))
        elif key == "cases":
            lines.append("cases:")
            for case in value:
                lines.append("  - title: " + yml_str(case["title"]))
                lines.append("    scope: " + yml_str(case["scope"]))
                lines.append("    region: " + yml_str(case["region"]))
                lines.append("    highlight: " + yml_str(case["highlight"]))
        else:
            lines.append(f"{key}: {yml_str(value)}")
    lines.append("---")
    return "\n".join(lines)


PRODUCTS = [
    {
        "slug": "steam-turbine",
        "category": "steam_turbine",
        "image": "/img/products/industrial-turbine.jpg",
        "en": {
            "title": "Steam Turbine Solutions (50 kW – 200 MW+) | Qingdao Quickleader",
            "subtitle": "Industrial and HTC steam turbines, spare parts, retrofit and maintenance",
            "description": "Qingdao Quickleader supplies steam turbines from 50 kW to 200 MW+, backed by NTC, HTC, Siemens and Jieneng partners. 20+ years of power plant 4S service.",
            "summary": "Steam turbines from 50 kW to 200 MW+, including condensing, back-pressure and extraction units. Sourced from NTC, HTC, Qingdao Jieneng and Siemens-licensed channels.",
            "faq": [
                {
                    "q": "What power range of steam turbines do you supply?",
                    "a": "We cover units from 50 kW up to 200 MW and above. This includes condensing, back-pressure, extraction and industrial drive turbines. For specific ratings and grid codes, we confirm the exact parameters with the OEM or our manufacturing partner before quotation."
                },
                {
                    "q": "Which OEMs or brands do you work with?",
                    "a": "Our supply channels include Nanjing Turbine Group (NTC), Hangzhou Turbine Group (HTC), Qingdao Jieneng Steam Turbine Group, and Siemens-technology steam turbine platforms. We can also cross-reference legacy units for equivalent spare parts."
                },
                {
                    "q": "Can you provide both new steam turbines and refurbished units?",
                    "a": "Yes. We supply new units, as well as factory-overhauled or refurbished turbines where the casing, rotor and blades are inspected to agreed standards. The scope and acceptance criteria are documented in the purchase specification."
                },
                {
                    "q": "What documentation is provided with the equipment?",
                    "a": "Standard documentation includes a bill of materials, material certificates, heat treatment records, balancing report, factory test report, inspection and test plan (ITP), and packing list. Third-party inspection by BV or SGS is available on request."
                },
                {
                    "q": "What is the typical lead time for a steam turbine package?",
                    "a": "For a standard industrial turbine, lead time is typically 8–16 weeks from order confirmation. For larger utility-class sets or customized packages, the lead time is usually 16–24 weeks. We state the exact schedule in the formal quotation."
                }
            ],
            "body": """## Application Scope

Steam turbines serve power generation, mechanical drive, cogeneration and process-steam applications. We support:

- Condensing and back-pressure turbines for power plants
- Extraction turbines for process industries
- High-speed mechanical drive turbines for compressors and pumps
- Retrofit and upgrade packages for existing turbine sets

## Service Coverage

Beyond supply, our 4S service model covers installation supervision, commissioning, vibration analysis, blade repair, bearing replacement and annual defect inspection."""
        },
        "zh": {
            "title": "汽轮机解决方案（50 kW – 200 MW+） | 青岛乾利得",
            "subtitle": "工业汽轮机、杭汽/南汽汽轮机、备件、改造与检修",
            "description": "青岛乾利得供应50 kW至200 MW+汽轮机，依托南汽、杭汽、西门子技术、青岛捷能等合作伙伴。20余年电站4S服务经验。",
            "summary": "50 kW至200 MW+汽轮机，包括凝汽式、背压式、抽汽式及工业驱动机组。采购渠道覆盖南汽、杭汽、青岛捷能及西门子技术平台。",
            "faq": [
                {
                    "q": "你们供应多大功率范围的汽轮机？",
                    "a": "我们覆盖50 kW到200 MW及以上的机组，包括凝汽式、背压式、抽汽式和工业驱动汽轮机。具体参数与电网要求，我们将在报价前与OEM或制造合作伙伴确认。"
                },
                {
                    "q": "合作的原厂品牌有哪些？",
                    "a": "我们的供应渠道包括南京汽轮机集团（南汽/NTC）、杭州汽轮机集团（杭汽/HTC）、青岛捷能汽轮机集团，以及西门子技术汽轮机平台。对于老旧机组，我们也可以交叉检索等效备件。"
                },
                {
                    "q": "能否提供新机和翻新机组？",
                    "a": "可以。我们供应全新机组，也提供工厂大修或翻新机组，其汽缸、转子、叶片等按约定标准检验。验收范围与标准将写入采购规范。"
                },
                {
                    "q": "设备附带哪些文件？",
                    "a": "标准文件包括物料清单、材质证书、热处理记录、动平衡报告、出厂试验报告、检验试验计划（ITP）和装箱单。可根据要求安排BV或SGS第三方检验。"
                },
                {
                    "q": "汽轮机成套设备的典型交付周期是多久？",
                    "a": "标准工业汽轮机一般在订单确认后8–16周；大型公用机组或定制化成套方案通常为16–24周。我们会在正式报价中列明确切交期。"
                }
            ],
            "body": """## 应用范围

汽轮机广泛用于发电、机械驱动、热电联产和工艺蒸汽领域。我们支持：

- 电站凝汽式、背压式汽轮机
- 抽汽式汽轮机用于工业流程
- 高速机械驱动汽轮机用于压缩机、泵
- 现有汽轮机组的改造与升级包

## 服务覆盖

除设备供应外，我们的4S服务模式还包括安装督导、调试、振动分析、叶片修复、轴承更换以及年度缺陷检查。"""
        },
        "it": {
            "title": "Soluzioni per Turbine a Vapore (50 kW – 200 MW+) | Qingdao Quickleader",
            "subtitle": "Turbine a vapore industriali, ricambi, retrofit e manutenzione",
            "description": "Qingdao Quickleader fornisce turbine a vapore da 50 kW a oltre 200 MW, con i partner NTC, HTC, Siemens e Jieneng. Oltre 20 anni di servizio 4S per centrali elettriche.",
            "summary": "Turbine a vapore da 50 kW a oltre 200 MW, incluse unità a condensazione, a contropressione e a estrazione. Canali di approvvigionamento NTC, HTC, Qingdao Jieneng e piattaforme Siemens.",
            "faq": [
                {
                    "q": "Qual è la gamma di potenza delle turbine a vapore che fornite?",
                    "a": "Copriamo unità da 50 kW fino a oltre 200 MW, incluse turbine a condensazione, a contropressione, a estrazione e a trazione industriale. Per potenze e codici di rete specifici, confermiamo i parametri esatti con l'OEM o il partner produttivo prima del preventivo."
                },
                {
                    "q": "Con quali OEM o marchi lavorate?",
                    "a": "I nostri canali di approvvigionamento includono Nanjing Turbine Group (NTC), Hangzhou Turbine Group (HTC), Qingdao Jieneng Steam Turbine Group e piattaforme con tecnologia Siemens. Possiamo anche ricercare ricambi equivalenti per unità legacy."
                },
                {
                    "q": "Potete fornire turbine nuove e revisionate?",
                    "a": "Sì. Forniamo unità nuove, nonché turbine revisionate o ricondizionate in fabbrica, dove carcassa, rotore e pale vengono ispezionati secondo standard concordati. Lo scope e i criteri di accettazione sono documentati nella specifica di acquisto."
                },
                {
                    "q": "Quali documentazioni sono fornite con le apparecchiature?",
                    "a": "La documentazione standard include distinta materiali, certificati dei materiali, registri di trattamento termico, rapporto di equilibratura, rapporto di prova in fabbrica, piano di ispezione e prova (ITP) e packing list. È disponibile l'ispezione di terze parti (BV/SGS) su richiesta."
                },
                {
                    "q": "Quali sono i tempi di consegna tipici per una turbina a vapore?",
                    "a": "Per una turbina industriale standard, il tempo di consegna è tipicamente di 8–16 settimane dalla conferma d'ordine. Per gruppi utility di grandi dimensioni o soluzioni personalizzate, solitamente 16–24 settimane. Il programma esatto viene indicato nel preventivo formale."
                }
            ],
            "body": """## Campo di Applicazione

Le turbine a vapore servono generazione di energia, azionamento meccanico, cogenerazione e applicazioni a vapore di processo. Supportiamo:

- Turbine a condensazione e a contropressione per centrali elettriche
- Turbine a estrazione per industrie di processo
- Turbine ad alta velocità per azionamento di compressori e pompe
- Pacchetti di retrofit e aggiornamento per gruppi esistenti

## Copertura del Servizio

Oltre alla fornitura, il nostro modello 4S include supervisione installazione, messa in servizio, analisi vibrazionale, riparazione pale, sostituzione cuscinetti e ispezione annuale dei difetti."""
        }
    },
    {
        "slug": "gas-turbine",
        "category": "gas_turbine",
        "image": "/img/products/gas-turbine.jpg",
        "en": {
            "title": "Gas Turbine Solutions | GE / Siemens Technology and Parts",
            "subtitle": "Heavy-duty and industrial gas turbines, hot-section parts, field service",
            "description": "Gas turbine supply, spare parts and field services for GE and Siemens-technology units. Quickleader provides hot-section components, blades, vanes and maintenance support.",
            "summary": "Heavy-duty and industrial gas turbines, hot-section components and field services for GE and Siemens-technology platforms. Parts include blades, vanes, combustors and filters.",
            "faq": [
                {
                    "q": "What gas turbine models do you support?",
                    "a": "We support GE-technology heavy-duty and aeroderivative gas turbines, as well as Siemens-technology industrial gas turbines. Specific models such as Frame 6, Frame 9 and STC-GV series are quoted based on frame size and operating regime."
                },
                {
                    "q": "Do you provide hot gas path components?",
                    "a": "Yes. We supply blades, vanes, combustors, transition pieces, seals and liners for hot-section maintenance. Material grades and coatings are quoted to match the OEM repair manual or the customer's technical specification."
                },
                {
                    "q": "Can you support GE / Siemens licensed units?",
                    "a": "Yes. We work with licensed manufacturers and qualified subcontractors for GE and Siemens-technology gas turbines. We verify origin, material certificates and repair records before shipment."
                },
                {
                    "q": "What about spare parts for older or obsolete units?",
                    "a": "For units that are no longer supported by the OEM, we source cross-reference or reverse-engineered parts from qualified Chinese and international suppliers. All non-OEM parts are offered with technical equivalence statements and quality documentation."
                },
                {
                    "q": "What service options do you offer?",
                    "a": "Our services include hot-section inspection, combustion tuning, rotor balancing support, boroscope inspection, filter and oil system maintenance, and on-site overhaul supervision. We can also arrange remote technical consultations."
                }
            ],
            "body": """## Application Scope

Gas turbines are used for baseload power, peaking plants, combined-cycle plants and industrial captive power. We support:

- Heavy-duty gas turbines for utility and industrial power generation
- Aeroderivative and industrial gas turbines for oil and gas, and manufacturing
- Combined-cycle (CCGT) and cogeneration plant upgrades

## Service Coverage

Our field service covers borescope inspection, hot-section repair planning, spare parts logistics, installation supervision and commissioning support."""
        },
        "zh": {
            "title": "燃气轮机解决方案 | GE / 西门子技术及备件",
            "subtitle": "重型及工业燃气轮机、热通道部件、现场服务",
            "description": "为GE技术和西门子技术燃气轮机提供整机、备件与现场服务。乾利得提供热通道叶片、导叶、燃烧室及维护支持。",
            "summary": "GE及西门子技术平台的重型/工业燃气轮机、热通道部件与现场服务。备件包括叶片、导叶、燃烧室、过渡段及过滤器。",
            "faq": [
                {
                    "q": "你们支持哪些燃气轮机型号？",
                    "a": "我们支持GE技术重型燃气轮机和航改型燃气轮机，以及西门子技术工业燃气轮机。Frame 6、Frame 9、STC-GV 等系列将根据机框尺寸和运行工况进行报价。"
                },
                {
                    "q": "是否提供热通道部件？",
                    "a": "是的。我们供应热通道检修用叶片、导叶、燃烧室、过渡段、密封件和衬套。材料等级与涂层按OEM维修手册或客户技术规范报价。"
                },
                {
                    "q": "能否支持GE / 西门子授权机组？",
                    "a": "可以。我们与GE、西门子技术燃气轮机的授权制造商及合格分包商合作，发货前核实产地、材质证书和维修记录。"
                },
                {
                    "q": "老旧或停产机组的备件怎么办？",
                    "a": "对于OEM已停止支持的机组，我们通过合格的中外供应商进行交叉检索或逆向工程备件。所有非OEM备件均提供技术等效说明及质量文件。"
                },
                {
                    "q": "提供哪些服务？",
                    "a": "我们的服务包括热通道检查、燃烧调整、转子平衡支持、孔探检查、滤油系统维护以及现场大修监理。同时可安排远程技术咨询。"
                }
            ],
            "body": """## 应用范围

燃气轮机用于基荷发电、调峰电站、联合循环电站及工业自备电厂。我们支持：

- 公用事业和工业发电用重型燃气轮机
- 油气、制造业用的航改型和工业燃气轮机
- 联合循环（CCGT）和热电联产机组升级

## 服务覆盖

我们的现场服务涵盖孔探检查、热通道检修方案、备件物流、安装督导和调试支持。"""
        },
        "it": {
            "title": "Soluzioni per Turbine a Gas | Tecnologia GE / Siemens e Ricambi",
            "subtitle": "Turbine a gas heavy-duty e industriali, parti hot-section, servizio in campo",
            "description": "Fornitura, ricambi e servizi in campo per turbine a gas con tecnologia GE e Siemens. Quickleader fornisce componenti hot-section, pale, palette e supporto manutentivo.",
            "summary": "Turbine a gas heavy-duty e industriali, componenti hot-section e servizi in campo per piattaforme GE e Siemens. I ricambi includono pale, palette, combustori e filtri.",
            "faq": [
                {
                    "q": "Quali modelli di turbine a gas supportate?",
                    "a": "Supportiamo turbine a gas heavy-duty e aeroderivative con tecnologia GE, nonché turbine a gas industriali con tecnologia Siemens. Modelli specifici come Frame 6, Frame 9 e serie STC-GV vengono quotati in base alla taglia e al regime di esercizio."
                },
                {
                    "q": "Fornite componenti del percorso gas caldo?",
                    "a": "Sì. Forniamo pale, palette, combustori, pezzi di transizione, tenute e rivestimenti per la manutenzione della hot-section. Gradi di materiale e rivestimenti vengono quotati in conformità al manuale di riparazione OEM o alla specifica tecnica del cliente."
                },
                {
                    "q": "Potete supportare unità con licenza GE / Siemens?",
                    "a": "Sì. Lavoriamo con produttori con licenza e subfornitori qualificati per turbine a gas con tecnologia GE e Siemens. Verifichiamo origine, certificati materiali e registri di riparazione prima della spedizione."
                },
                {
                    "q": "E i ricambi per unità più vecchie o obsolete?",
                    "a": "Per unità non più supportate dall'OEM, ricerciamo ricambi cross-reference o reverse-engineered da fornitori cinesi e internazionali qualificati. Tutti i ricambi non OEM sono offerti con dichiarazione di equivalenza tecnica e documentazione di qualità."
                },
                {
                    "q": "Quali opzioni di servizio offrite?",
                    "a": "I nostri servizi includono ispezione hot-section, messa a punto della combustione, supporto bilanciamento rotore, ispezione endoscopica, manutenzione filtri e sistema olio, e supervisione alla revisione in campo. Possiamo anche organizzare consulenze tecniche remote."
                }
            ],
            "body": """## Campo di Applicazione

Le turbine a gas sono utilizzate per potenza di base, impianti di picco, cicli combinati e energia cattiva industriale. Supportiamo:

- Turbine a gas heavy-duty per generazione di energia utility e industriale
- Turbine aeroderivative e industriali per oil and gas e manifatturiero
- Aggiornamenti per impianti a ciclo combinato (CCGT) e cogenerazione

## Copertura del Servizio

Il nostro servizio in campo copre ispezione endoscopica, pianificazione riparazione hot-section, logistica ricambi, supervisione installazione e supporto alla messa in servizio."""
        }
    },
    {
        "slug": "boiler",
        "category": "boiler",
        "image": "/img/products/boiler.jpg",
        "en": {
            "title": "Boiler Solutions | Coal, Biomass, HRSG and Spare Parts",
            "subtitle": "Power plant boilers, heat recovery steam generators and boiler replacement parts",
            "description": "Qingdao Quickleader supplies coal-fired, biomass and HRSG boilers, plus pressure parts, burners, grates and tube bundles. Partner brands include Jinan, Wuxi and Tai'an boiler groups.",
            "summary": "Coal-fired, biomass-fired and HRSG boilers for power and process steam. Replacement pressure parts, burners, tube bundles and support from Jinan, Wuxi and Tai'an boiler groups.",
            "faq": [
                {
                    "q": "What types of boilers do you supply?",
                    "a": "We supply coal-fired boilers, biomass-fired boilers, waste-heat boilers (HRSG) for combined-cycle plants, and package boilers for process steam. The scope can be boiler island only, or a full EPC power plant package."
                },
                {
                    "q": "What fuel types are supported?",
                    "a": "Our boiler packages support bituminous coal, sub-bituminous coal, lignite, biomass pellets, rice husk, wood chips, bagasse, and process off-gas. Fuel analysis is required to size the furnace, grate and dust-removal system."
                },
                {
                    "q": "Do you supply HRSG for combined-cycle plants?",
                    "a": "Yes. We provide horizontal and vertical HRSG units for gas-turbine combined-cycle and cogeneration plants. We design around the gas turbine exhaust temperature, mass flow and steam pressure requirements."
                },
                {
                    "q": "What pressure and temperature ratings are available?",
                    "a": "Utility and industrial boiler ratings are typically quoted from low-pressure process steam up to high-pressure, high-temperature supercritical parameters. The exact rating is selected based on the turbine inlet conditions and local grid code."
                },
                {
                    "q": "Can you provide replacement parts for existing boilers?",
                    "a": "Yes. We supply membrane water walls, economizers, superheaters, reheaters, burners, grates, headers, valves and instrumentation. We use drawings or samples to match replacement parts to existing installations."
                }
            ],
            "body": """## Application Scope

Boilers are the heart of thermal power plants and process steam systems. We support:

- Coal-fired power plants and industrial captive power
- Biomass power plants and waste-to-energy projects
- Heat recovery steam generators behind gas turbines
- Retrofit and replacement of boiler pressure parts

## Service Coverage

Our boiler services include performance calculation, pressure-part design, material selection, installation supervision, hydrostatic testing, commissioning and annual inspection support."""
        },
        "zh": {
            "title": "锅炉解决方案 | 燃煤、生物质、余热锅炉及备件",
            "subtitle": "电站锅炉、余热锅炉、锅炉受压部件与替换件",
            "description": "青岛乾利得供应燃煤锅炉、生物质锅炉、余热锅炉（HRSG）及受压部件、燃烧器、炉排、管束。合作品牌包括济南、无锡、泰安锅炉集团。",
            "summary": "用于发电和工艺蒸汽的燃煤、生物质及余热锅炉（HRSG）。提供受压部件、燃烧器、管束等替换件，合作品牌包括济南、无锡、泰安锅炉集团。",
            "faq": [
                {
                    "q": "你们供应哪些类型的锅炉？",
                    "a": "我们供应燃煤锅炉、生物质锅炉、燃气轮机联合循环用余热锅炉（HRSG），以及工艺蒸汽用快装锅炉。供货范围可以是锅炉岛，也可以是完整电站EPC包。"
                },
                {
                    "q": "支持哪些燃料类型？",
                    "a": "我们的锅炉方案支持烟煤、次烟煤、褐煤、生物质颗粒、稻壳、木片、甘蔗渣以及工艺尾气。需要提供燃料分析，以便确定炉膛、炉排和除尘系统的尺寸。"
                },
                {
                    "q": "是否提供联合循环用余热锅炉？",
                    "a": "是的。我们为燃气轮机联合循环和热电联产项目提供卧式和立式余热锅炉，设计依据燃气轮机排气温度、质量流量和蒸汽压力参数。"
                },
                {
                    "q": "压力和温度等级范围是多少？",
                    "a": "工业和电站锅炉通常从低压工艺蒸汽到高温高压乃至超临界参数。具体等级根据汽轮机进口参数和当地电网规范选择。"
                },
                {
                    "q": "能否提供现有锅炉的替换件？",
                    "a": "可以。我们供应膜式水冷壁、省煤器、过热器、再热器、燃烧器、炉排、集箱、阀门及仪表。我们可根据图纸或实物测绘匹配替换件。"
                }
            ],
            "body": """## 应用范围

锅炉是火电厂和工艺蒸汽系统的核心。我们支持：

- 燃煤电站和工业自备电厂
- 生物质电站和垃圾/废弃物发电项目
- 燃气轮机后余热锅炉
- 锅炉受压部件的改造与替换

## 服务覆盖

我们的锅炉服务包括性能计算、受压部件设计、选材、安装监理、水压试验、调试和年度检查支持。"""
        },
        "it": {
            "title": "Soluzioni per Caldaie | Carbone, Biomassa, HRSG e Ricambi",
            "subtitle": "Caldaie per centrali elettriche, generatori di vapore a recupero e parti di ricambio",
            "description": "Qingdao Quickleader fornisce caldaie a carbone, a biomassa e HRSG, oltre a parti in pressione, bruciatori, griglie e fasci tubieri. Marchi partner: Jinan, Wuxi e Tai'an Boiler Group.",
            "summary": "Caldaie a carbone, a biomassa e HRSG per energia e vapore di processo. Ricambi per parti in pressione, bruciatori, fasci tubieri e supporto dai gruppi Jinan, Wuxi e Tai'an.",
            "faq": [
                {
                    "q": "Che tipi di caldaie fornite?",
                    "a": "Forniamo caldaie a carbone, a biomassa, caldaie a recupero (HRSG) per impianti a ciclo combinato, e caldaie package per vapore di processo. Lo scope può essere solo l'isola caldaia o un pacchetto EPC completo."
                },
                {
                    "q": "Quali tipi di combustibile sono supportati?",
                    "a": "I nostri pacchetti caldaia supportano carbone bituminoso, sub-bituminoso, lignite, pellet di biomassa, lolla di riso, cippato di legno, bagassa e gas di processo. È richiesta l'analisi del combustibile per dimensionare forno, griglia e sistema di depolverazione."
                },
                {
                    "q": "Fornite HRSG per impianti a ciclo combinato?",
                    "a": "Sì. Forniamo HRSG orizzontali e verticali per cicli combinati a turbina a gas e cogenerazione. Progettiamo in base alla temperatura di scarico, alla portata massica e ai requisiti di pressione vapore."
                },
                {
                    "q": "Quali pressioni e temperature sono disponibili?",
                    "a": "Le caldaie utility e industriali vengono tipicamente quotate da vapore di processo a bassa pressione fino a parametri supercritici ad alta pressione e temperatura. Il rating esatto viene selezionato in base alle condizioni di ingresso della turbina e al codice di rete locale."
                },
                {
                    "q": "Potete fornire parti di ricambio per caldaie esistenti?",
                    "a": "Sì. Forniamo pareti membrana, economizzatori, surriscaldatori, riscaldatori, bruciatori, griglie, collettori, valvole e strumentazione. Utilizziamo disegni o campioni per abbinare i ricambi alle installazioni esistenti."
                }
            ],
            "body": """## Campo di Applicazione

Le caldaie sono il cuore delle centrali termoelettriche e dei sistemi a vapore di processo. Supportiamo:

- Centrali a carbone e energia cattiva industriale
- Impianti a biomassa e waste-to-energy
- Generatori di vapore a recupero a valle di turbine a gas
- Retrofit e sostituzione di parti in pressione

## Copertura del Servizio

I nostri servizi per caldaie includono calcolo prestazioni, progettazione parti in pressione, selezione materiali, supervisione installazione, prova idrostatica, messa in servizio e supporto ispezione annuale."""
        }
    },
    {
        "slug": "power-plant-service",
        "category": "power_plant_service",
        "image": "/img/products/epc.jpg",
        "en": {
            "title": "Power Plant Service & EPC | 4S Center for Your Plant",
            "subtitle": "EPC contracting, installation, overhaul, spare parts and annual inspection",
            "description": "Qingdao Quickleader provides power plant EPC, 4S service, installation, commissioning, overhaul and spare parts management. One-stop partner for steam, gas and biomass plants.",
            "summary": "Turnkey EPC, installation, commissioning, overhaul, spare parts and annual inspection for steam, gas and biomass power plants. One-stop 4S service center.",
            "faq": [
                {
                    "q": "What does your EPC service include?",
                    "a": "Our EPC scope covers feasibility study, basic and detailed engineering, equipment procurement, construction management, installation, commissioning, performance testing and handover. We can act as the main EPC contractor or supply equipment under an EPCM arrangement."
                },
                {
                    "q": "Do you provide on-site maintenance and overhaul?",
                    "a": "Yes. We send qualified engineers and supervisors to site for scheduled maintenance, major overhaul, defect rectification and performance upgrades. We can also mobilize specialist tooling and OEM field service partners."
                },
                {
                    "q": "What is the 4S service model?",
                    "a": "4S stands for Sale, Spare Parts, Service and Survey. It is a one-stop model adapted from the automotive industry: we supply the plant, keep critical spare parts in stock, perform maintenance, and carry out annual inspection and reporting."
                },
                {
                    "q": "How do you handle emergency breakdowns?",
                    "a": "For critical failures, we activate a rapid response process: diagnose the fault, identify the required spare parts, arrange emergency air freight or local sourcing, and dispatch an engineer to site for supervision. Response times depend on visa, travel and parts availability."
                },
                {
                    "q": "Can you support remote diagnostics and technical training?",
                    "a": "Yes. We can provide remote diagnostics based on operating data, vibration and temperature logs, and video conference guidance. We also offer technical training for plant operators and maintenance teams on equipment operation and routine inspection."
                }
            ],
            "body": """## Service Portfolio

Our 4S service center covers the full plant lifecycle:

- Feasibility and conceptual engineering
- Equipment procurement and quality inspection
- Civil, mechanical and electrical installation
- Commissioning, performance testing and handover
- Spare parts management and inventory planning
- Scheduled maintenance, overhaul and upgrade
- Annual defect inspection and condition assessment

## Project Delivery Models

- **EPC** – turnkey engineering, procurement and construction
- **EPCM** – engineering and procurement management with local construction
- **Supply-only** – main equipment or spare parts with documentation
- **Service-only** – inspection, maintenance and technical support"""
        },
        "zh": {
            "title": "电站服务与EPC | 电站4S服务中心",
            "subtitle": "EPC总承包、安装调试、大修、备件管理与年度巡检",
            "description": "青岛乾利得提供电站EPC、4S服务、安装调试、检修、备件管理。汽轮机、燃气轮机、生物质电站一站式合作伙伴。",
            "summary": "汽轮机、燃气轮机、生物质电站的交钥匙EPC、安装调试、大修、备件与年度巡检。一站式电站4S服务中心。",
            "faq": [
                {
                    "q": "你们的EPC服务包含哪些内容？",
                    "a": "我们的EPC范围涵盖可行性研究、基础设计和详细设计、设备采购、施工管理、安装、调试、性能试验及移交。我们可以作为总包方，也可以在EPCM模式下提供设备采购管理服务。"
                },
                {
                    "q": "是否提供现场维护与大修？",
                    "a": "是的。我们派遣合格工程师和监理到现场进行计划性维护、大修、缺陷整改和性能升级。我们也可以调动专用工具和原厂现场服务合作伙伴。"
                },
                {
                    "q": "4S服务模式是什么？",
                    "a": "4S指 Sale（销售）、Spare Parts（备件）、Service（服务）、Survey（巡检）。我们借鉴汽车行业4S模式，为客户提供设备、备件、维护和年度检查报告的一站式服务。"
                },
                {
                    "q": "紧急故障如何处理？",
                    "a": "对于关键故障，我们启动快速响应流程：诊断故障、确定所需备件、安排加急空运或本地采购，并派遣工程师到现场指导。响应时间取决于签证、差旅和备件可得性。"
                },
                {
                    "q": "是否支持远程诊断和技术培训？",
                    "a": "是的。我们可以基于运行数据、振动和温度记录进行远程诊断，并通过视频会议提供指导。我们也为电厂运行和维护人员提供设备操作和日常检查技术培训。"
                }
            ],
            "body": """## 服务范围

我们的4S服务中心覆盖电站全生命周期：

- 可行性研究和概念设计
- 设备采购与质量检验
- 土建、机械和电气安装
- 调试、性能试验及移交
- 备件管理与库存规划
- 计划性维护、大修和升级改造
- 年度缺陷检查与状态评估

## 项目交付模式

- **EPC** – 交钥匙工程总承包
- **EPCM** – 工程与采购管理，当地施工
- **纯设备供应** – 主机或备件，附文件
- **纯服务** – 检查、维护和技术支持"""
        },
        "it": {
            "title": "Servizio Centrale & EPC per Centrali Elettriche | Centro 4S",
            "subtitle": "Contratti EPC, installazione, revisione, ricambi e ispezione annuale",
            "description": "Qingdao Quickleader fornisce EPC, servizio 4S, installazione, messa in servizio, revisione e gestione ricambi per centrali a vapore, a gas e a biomassa. Partner one-stop.",
            "summary": "EPC chiavi in mano, installazione, messa in servizio, revisione, ricambi e ispezione annuale per centrali a vapore, a gas e a biomassa. Centro di servizio 4S one-stop.",
            "faq": [
                {
                    "q": "Cosa include il vostro servizio EPC?",
                    "a": "Il nostro scope EPC copre studio di fattibilità, ingegneria di base e di dettaglio, procurement, gestione costruzioni, installazione, messa in servizio, prove di prestazione e consegna. Possiamo agire come EPC contractor principale o fornire attrezzature in regime EPCM."
                },
                {
                    "q": "Fornite manutenzione e revisione in campo?",
                    "a": "Sì. Inviamo ingegneri e supervisori qualificati in sito per manutenzione programmata, revisione generale, eliminazione difetti e upgrade prestazionali. Possiamo anche mobilitare attrezzature specializzate e partner di service OEM."
                },
                {
                    "q": "Cos'è il modello di servizio 4S?",
                    "a": "4S sta per Vendita (Sale), Ricambi (Spare Parts), Servizio (Service) e Ispezione (Survey). È un modello one-stop adattato dall'industria automobilistica: forniamo l'impianto, teniamo ricambi critici a magazzino, eseguiamo manutenzione e redigiamo ispezione annuale."
                },
                {
                    "q": "Come gestite le emergenze per guasti?",
                    "a": "Per guasti critici attiviamo un processo di risposta rapida: diagnosi del guasto, identificazione ricambi necessari, organizzazione di trasporto aereo urgente o sourcing locale, e invio di un ingegnere in sito per supervisione. I tempi di risposta dipendono da visti, viaggi e disponibilità ricambi."
                },
                {
                    "q": "Supportate diagnostica remota e formazione tecnica?",
                    "a": "Sì. Possiamo fornire diagnostica remota basata su dati operativi, log di vibrazione e temperatura, e guida via videoconferenza. Offriamo anche formazione tecnica per operatori e team di manutenzione su operazione e ispezione di routine."
                }
            ],
            "body": """## Portfolio di Servizio

Il nostro centro di servizio 4S copre l'intero ciclo di vita dell'impianto:

- Fattibilità e ingegneria concettuale
- Procurement e ispezione qualità attrezzature
- Installazione civile, meccanica ed elettrica
- Messa in servizio, prove di prestazione e consegna
- Gestione ricambi e pianificazione magazzino
- Manutenzione programmata, revisione e upgrade
- Ispezione annuale difetti e valutazione condizione

## Modelli di Consegna Progetto

- **EPC** – ingegneria, approvvigionamento e costruzione chiavi in mano
- **EPCM** – ingegneria e procurement management con costruzione locale
- **Solo fornitura** – apparecchiature principali o ricambi con documentazione
- **Solo servizio** – ispezione, manutenzione e supporto tecnico"""
        }
    }
]


SECTION_INDEXES = {
    "products": {
        "en": ("Products & Services", "Power plant equipment and 4S service solutions from Qingdao Quickleader"),
        "zh": ("产品与服务", "青岛乾利得电站设备及4S服务解决方案"),
        "it": ("Prodotti e Servizi", "Apparecchiature e servizi 4S per centrali elettriche da Qingdao Quickleader"),
        "type": "products"
    },
    "faq": {
        "en": ("Frequently Asked Questions", "Answers to the most common questions about our power plant equipment and services"),
        "zh": ("常见问题", "关于我们电站设备与服务最常见问题的解答"),
        "it": ("Domande Frequenti", "Risposte alle domande più comuni sulle apparecchiature e sui servizi per centrali elettriche"),
        "type": "faq"
    },
    "cases": {
        "en": ("Project Cases", "Representative project types and applications we support"),
        "zh": ("项目案例", "我们支持的代表性项目类型与应用"),
        "it": ("Casi di Progetto", "Tipologie di progetto rappresentative e applicazioni che supportiamo"),
        "type": "cases"
    }
}


CERTIFICATES = {
    "en": {
        "title": "Certifications | Bureau Veritas, CE, SGS",
        "subtitle": "International third-party certifications backing our quality system",
        "description": "Qingdao Quickleader is certified by Bureau Veritas (BV), CE and SGS. View our certification gallery and download inspection reports.",
        "certificates": [
            {"name": "Bureau Veritas Factory Inspection", "image": "/img/certs/BV1-1.JPG", "issuer": "Bureau Veritas", "scope": "Factory inspection and quality system audit for power plant equipment manufacturing."},
            {"name": "CE Certification for Equipment", "image": "/img/certs/CE证书.jpg", "issuer": "Notified Body", "scope": "CE marking for applicable electrical and mechanical equipment supplied to the EU market."},
            {"name": "SGS Supplier Audit", "image": "/img/certs/SGS2.JPG", "issuer": "SGS", "scope": "Supplier capability and product quality assessment for export projects."},
            {"name": "CE Power Plant Certificate", "image": "/img/certs/CE POWER PLANT.jpg", "issuer": "Notified Body", "scope": "CE documentation for power plant systems and packages."}
        ]
    },
    "zh": {
        "title": "资质认证 | 必维（BV）、CE、SGS",
        "subtitle": "国际第三方认证支持我们的质量体系",
        "description": "青岛乾利得通过必维（BV）、CE和SGS认证。查看认证图库并下载检验报告。",
        "certificates": [
            {"name": "必维工厂检验", "image": "/img/certs/BV1-1.JPG", "issuer": "Bureau Veritas（必维）", "scope": "电站设备制造的工厂检验与质量体系审核。"},
            {"name": "设备CE认证", "image": "/img/certs/CE证书.jpg", "issuer": "公告机构", "scope": "面向欧盟市场的适用电气与机械设备的CE标志。"},
            {"name": "SGS供应商审核", "image": "/img/certs/SGS2.JPG", "issuer": "SGS", "scope": "出口项目的供应商能力与产品质量评估。"},
            {"name": "电站CE认证", "image": "/img/certs/CE POWER PLANT.jpg", "issuer": "公告机构", "scope": "电站系统及成套设备的CE文件。"}
        ]
    },
    "it": {
        "title": "Certificazioni | Bureau Veritas, CE, SGS",
        "subtitle": "Certificazioni internazionali di terze parti a supporto del nostro sistema qualità",
        "description": "Qingdao Quickleader è certificata da Bureau Veritas (BV), CE e SGS. Visualizza la galleria delle certificazioni e scarica i rapporti di ispezione.",
        "certificates": [
            {"name": "Ispezione di Fabbrica Bureau Veritas", "image": "/img/certs/BV1-1.JPG", "issuer": "Bureau Veritas", "scope": "Ispezione di fabbrica e audit del sistema qualità per la produzione di apparecchiature per centrali elettriche."},
            {"name": "Certificazione CE per Attrezzature", "image": "/img/certs/CE证书.jpg", "issuer": "Organismo Notificato", "scope": "Marcatura CE per apparecchiature elettriche e meccaniche applicabili destinate al mercato UE."},
            {"name": "Audit Fornitore SGS", "image": "/img/certs/SGS2.JPG", "issuer": "SGS", "scope": "Valutazione della capacità fornitore e della qualità prodotto per progetti export."},
            {"name": "Certificato CE Power Plant", "image": "/img/certs/CE POWER PLANT.jpg", "issuer": "Organismo Notificato", "scope": "Documentazione CE per sistemi e pacchetti power plant."}
        ]
    }
}


CASES = {
    "en": [
        {"title": "Steam Turbine Overhaul & Spare Parts Supply", "scope": "Major overhaul of a 50 MW condensing steam turbine including rotor inspection, blade replacement and bearing refurbishment.", "region": "Southeast Asia", "highlight": "Reduced downtime by coordinating parts and specialist tooling together."},
        {"title": "Biomass Power Plant EPC", "scope": "Turnkey EPC of a 10 MW biomass-fired power plant including boiler, turbine, generator and electrical systems.", "region": "Central Asia", "highlight": "Completed commissioning and performance test within the contracted window."},
        {"title": "Gas Turbine Hot-Section Maintenance", "scope": "Hot-section inspection, combustion hardware replacement and reassembly supervision for a Frame 6B-class unit.", "region": "Middle East", "highlight": "Sourced qualified hot-section parts and dispatched field engineers."},
        {"title": "Coal-Fired Boiler Retrofit", "scope": "Replacement of water-wall tubes, economizer and burner upgrade for an existing industrial boiler.", "region": "Africa", "highlight": "Improved availability and efficiency through tailored pressure-part design."}
    ],
    "zh": [
        {"title": "汽轮机大修与备件供应", "scope": "一台50 MW凝汽式汽轮机大修，包括转子检查、叶片更换和轴承翻新。", "region": "东南亚", "highlight": "通过同步协调备件和专用工具，缩短停机时间。"},
        {"title": "生物质电站EPC", "scope": "10 MW生物质发电厂交钥匙EPC，包括锅炉、汽轮机、发电机及电气系统。", "region": "中亚", "highlight": "在合同窗口内完成调试和性能试验。"},
        {"title": "燃气轮机热通道维护", "scope": "Frame 6B级燃气轮机热通道检查、燃烧硬件更换和回装监理。", "region": "中东", "highlight": "采购合格热通道部件并派遣现场工程师。"},
        {"title": "燃煤锅炉改造", "scope": "现有工业锅炉水冷壁管更换、省煤器更新及燃烧器升级。", "region": "非洲", "highlight": "通过定制化受压部件设计提高可用率和效率。"}
    ],
    "it": [
        {"title": "Overhaul Turbina a Vapore e Fornitura Ricambi", "scope": "Revisione generale di una turbina a vapore a condensazione da 50 MW, inclusa ispezione rotore, sostituzione pale e revisione cuscinetti.", "region": "Sud-Est Asiatico", "highlight": "Riduzione del downtime coordinando ricambi e attrezzature specializzate."},
        {"title": "EPC Centrale a Biomassa", "scope": "EPC chiavi in mano di una centrale a biomassa da 10 MW, inclusa caldaia, turbina, generatore e sistemi elettrici.", "region": "Asia Centrale", "highlight": "Commissioning e prove di prestazione completate entro la finestra contrattuale."},
        {"title": "Manutenzione Hot-Section Turbina a Gas", "scope": "Ispezione hot-section, sostituzione hardware combustione e supervisione rimontaggio per unità classe Frame 6B.", "region": "Medio Oriente", "highlight": "Sourcing di parti hot-section qualificate e invio ingegneri in campo."},
        {"title": "Retrofit Caldaia a Carbone", "scope": "Sostituzione tubi parete acqua, economizzatore e upgrade bruciatori per una caldaia industriale esistente.", "region": "Africa", "highlight": "Miglioramento disponibilità ed efficienza tramite progettazione su misura delle parti in pressione."}
    ]
}


def write_product_pages():
    for p in PRODUCTS:
        for lang in ("en", "zh", "it"):
            d = p[lang]
            folder = BASE / "content" / lang / "products"
            folder.mkdir(parents=True, exist_ok=True)
            fields = {
                "title": d["title"],
                "subtitle": d["subtitle"],
                "description": d["description"],
                "type": "products",
                "category": p["category"],
                "image": p["image"],
                "summary": d["summary"],
                "faq": d["faq"]
            }
            text = make_frontmatter(fields) + "\n\n" + d["body"]
            (folder / f"{p['slug']}.md").write_text(text, encoding="utf-8")


def write_section_indexes():
    for section, data in SECTION_INDEXES.items():
        for lang in ("en", "zh", "it"):
            title, subtitle = data[lang]
            folder = BASE / "content" / lang / section
            folder.mkdir(parents=True, exist_ok=True)
            fields = {
                "title": title,
                "subtitle": subtitle,
                "type": data["type"]
            }
            if section == "cases":
                fields["cases"] = CASES[lang]
            text = make_frontmatter(fields) + "\n"
            (folder / "_index.md").write_text(text, encoding="utf-8")


def write_certifications():
    for lang in ("en", "zh", "it"):
        d = CERTIFICATES[lang]
        folder = BASE / "content" / lang
        folder.mkdir(parents=True, exist_ok=True)
        fields = {
            "title": d["title"],
            "subtitle": d["subtitle"],
            "description": d["description"],
            "type": "certifications",
            "certificates": d["certificates"]
        }
        text = make_frontmatter(fields) + "\n\n## " + ("Certification Gallery" if lang == "en" else ("认证图库" if lang == "zh" else "Galleria Certificazioni")) + "\n\nAll certifications are available for download or third-party verification on request.\n"
        (folder / "certifications.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_product_pages()
    write_section_indexes()
    write_certifications()
    print("Content generated successfully.")
