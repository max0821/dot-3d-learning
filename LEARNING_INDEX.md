# DOTS 人物建模學習記憶：方法、失敗與恢復索引

更新：2026-10-30。這是可查閱、可重做的外部記憶，不代表模型權重自我訓練，也不保證未來會自動讀到。**每輪開工必須先讀本頁及對應 NOTES，再決定實驗。**

## 先讀這六條，避免白學與重犯

1. **方法運作 ≠ 造型通過。** 原生操作回傳 FINISHED、網格封閉、版本增加、數值改善，都不能代替原圖與四向渲染驗收。
2. **看到來源的哪一步就記哪一步。** 正文、圖解、離散影片影格、搜尋節錄、未播放影片分開記；不將字幕或章節標題寫成看過動作。
3. **先辨認可見邊界、遮擋與體積，再選方法。** 光影線不是髮束分界；內部交界不是第二個尖端；側圖不標準不能量出唯一深度。
4. **停止條件：同一錯誤構造連續微調仍失敗，就停止。** 不再加厚矩形叉片、不在圓管上疊深度假裝布面、不用任意頂點權重冒稱作者筆刷。
5. **先最小重現，再適配原角色。** 保存不改的 A、只改明確因素的 B、失敗例與恢復腳本；多因素一起改只能叫方法比較，不能宣稱單一因果。
6. **每輪留下一個可重做的測試與下一個問題。** 下一輪先回顧最近失敗；每完成一階段，再回做較早的方法卡。能從記錄恢復並解釋限制，才算知識有留下。

## 目前位置與恢復錨點

- 使用者指定順序：**頭部整體 → 頭髮 → 五官 → 身體四肢 → 穿著**。目前在頭髮；衣物為既有學習存檔，不搶先延續。
- 保留人物：`iteration04`（模型未包含）。可見頰顎暫保留；顱頂／後頰／後腦未驗證，**不是完美、不是使用者驗收**。已記錄 SHA256：`35cd1b71c9d288029d93d0fdb8d9741d62a5151bc3bc459ab48c789092b5aaa6`；修改前需重新核對。
- 最新更正：[H1輸入契約撤回](experiments/forelock-support-h1/NOTES.md)：指定audit B不是有限根片，無合格後邊界；未射線或接根，沒有新模型／圖。F25雙驗收原則保留，原H1規格撤回。
- 最近局部實作：[單尖面片最近表面適配](experiments/forelock-surface-strip/NOTES.md)，整束Closest塌縮失敗，不升基線。
- 最新限制補充：[F27接收面門檻](experiments/forelock-support-gate/NOTES.md)：現有主束／鄰束亦5/5未命中；撤回重複餘量延伸。無新模型／圖，下一步改研究寬前殼與主量共同面轉向。
- 使用者提供的作品展示入口：[Max.0821 的 Sketchfab](https://sketchfab.com/Max.0821)。已核對公開目錄名稱及部分作品連結，詳見 [街景與寧夏歷史](history/SCENE_LEARNING_HISTORY.md)；目錄存在不等於逐件驗收。

- 新增來源比較（研究未實作）：Snowstorm寬扁管可作底量材料，後續合併／重排與保留獨立細束是不同決策。僅實讀作者文字，四張中間圖未取得，不能據此猜Remesh或稱已學會接根；見[F7來源補充](experiments/hair-mass-overlap-research/NOTES.md)。

### 狀態字典
- **方法已驗證（局部）**：有實際操作與對照，僅限記錄的機制及條件。
- **造型未通過**：已有實物，但未符合目標；保留失敗、不替代較佳基線。
- **研究未實作**：已有來源或分析，沒有對應新模型；不能用舊圖冒充。
- **歷史要求／未核實**：歷史紀錄曾提出，尚缺可核對檔案或成果。

## 一、頭部整體：形體比增加細分重要

### H1｜連續控制籠、不同頭型的選擇
**來源／觀看紀錄：** Karan Shah [低模忍者第36–43步](https://design.tutsplus.com/tutorials/creating-a-low-poly-ninja-game-character-using-blender-part-1--cg-16132)，含第38步實圖；[CLIP STUDIO Q版頭型](https://www.clipstudio.net/how-to-draw/archives/155423) 與 [Cabral 卡通臉](https://design.tutsplus.com/articles/cartoon-fundamentals-how-to-draw-a-cartoon-face-correctly--vector-15792) 的實際插圖。不是照搬成人比例。

- **適用：** 用少量連續面控制顱部、頰部與顎部，先比較短圓、長窄等頭型，再選符合原圖的可見輪廓。
- **狀態：方法已驗證／造型未通過。** A 下顎過窄，B 回補臉頰只比 A 合理，沒有證明優於04。
- **戒條：** 不把「更尖、更瘦、更平滑」當進步；正面成立不等於側面體積成立。
- **下一步：** 若重開頭部，先提出新的可見差異證據，不猜被頭髮遮住的深度。
- **恢復：** [頭型比較](experiments/head-form-study/NOTES.md)、[頭部平面](experiments/head-plane-study/NOTES.md)、[頰部局部變形](experiments/head-cheek-transition/NOTES.md)、[證據稽核](experiments/head-evidence-audit/NOTES.md)。原實驗曾保存 before/after 或 ABC；本公開倉庫包含筆記及文末有效連結列出的精選圖，不包含原模型與建模腳本。

### H2｜頭部平面與局部 Move 的適配邊界
[Proko 頭部量塊](https://stanprokopenko.com/2012/08/video-draw-head-angle-1/) 與 [Kenny 頭部平面](https://kennysarts.gumroad.com/p/planes-of-the-head) 支持區分顱體、顎體與平面；[頭套建模圖解](https://www.fursuitmak.ing/tutorials/3Dheadbase.php) 的局部 Move 與連續面、[Autodesk Soft Selection](https://help.autodesk.com/cloudhelp/2020/ENU/MayaLT-GettingStarted/files/GUID-DD4CF5ED-5017-4934-8678-76AAE1DAC51B.htm) 支持局部過渡。

**結果：** 提高後下顎造成楔形，後續仍機械平底；增加頰部飽滿也未可靠勝過04。這些是方法適配試驗，非作者示範本角色。不要全局 Smooth 掩蓋錯誤平面。相關恢復入口同 H1。

## 二、頭髮：現在的主線

### F1｜先髮量與遮擋，後束與細節
**來源：** [Dan Eder](https://80.lv/articles/guide-sculpting-stylized-hair-in-zbrush) 的主量塊／表面束 GIF 離散影格與 clipping 對照；[Leah McEwen](https://leahmcewen.artstation.com/blog/dzzZR/breaking-down-references-for-3d-hair-creation) 五欄拆解；[Boehmy](https://www.zbrushcentral.com/t/how-to-sculpted-hair/373187) Step1–4 圖解、支承擷取後再推拉。這些不是同款短尖髮的完整逐筆示範。

- **適用：** 可見尖端很多，但根部和層序不明；先區分外輪廓、主束、負空間、次束。可見上方白縫不代表下方深色交界也要開洞。
- **狀態：分析有用；新主髮量造型未通過。** 移除底層能消掉額前楔片，卻露頭皮；前弧束可增加遮擋，卻仍懸浮或尖端接錯。
- **戒條：** 不拿新增束數掩蓋插接；不要讓每束兩端都尖；從裸頭加管不等於在既有髮量上整理束。
- **下一步：** 找到造型相近的尖髮作者實際操作，選一個可見根→主量→尖端區練習；遮住的根位置明標假設。
- **恢復：** [遮擋診斷](experiments/diagonal-clump-study/NOTES.md)、[參考拆解](experiments/hair-occlusion-analysis/NOTES.md)、[前額層次](experiments/front-hair-layer/NOTES.md)、[根研究](experiments/hair-root-research/NOTES.md)、[擷取試驗](experiments/supported-hair-root/NOTES.md)。

### F2｜曲線路徑、半徑、截面、切線分開控制
**來源：** [Danny Mac Step3–4](https://blog.cgcookie.com/posts/how-to-model-hair-in-blender/)、[Antoine Dupuis 圖集](https://antoinedupuis.artstation.com/projects/rRqEAa)、[Danyl 作者回答](https://blender.stackexchange.com/questions/101112/how-can-i-create-easily-editable-stylized-hairs-and-fur)、[rogodigital 路徑示範](https://rogodigital.design/tutorials/project-a-shape-along-a-path/)、[六色截面](https://note.com/rikuhayasaka/n/n5ab4a25233d1)、[Autodesk 切線圖解](https://help.autodesk.com/cloudhelp/2021/ENU/PWRM-ReferenceHelp/files/GUID-DAD261C5-F099-430C-BF0A-BB5C06CAFDBC.htm)。

- **適用：** 長束、弧束、可編輯局部髮流。長髮教學提供通用控制方法，不直接給短寬尖髮答案。
- **狀態：方法已驗證；目標造型未通過。** 改半徑可減根肩鼓包；閉合截面可增加體積；切線控制彎度。仍有葉片、端帽、內彎夾窄及扁根。
- **戒條：** 封閉不等於自然；根半徑不是接合；調切線不能補缺少的主髮量。鏡頭沿長軸時縮短，不可換鏡頭後稱模型改善。
- **下一步：** 先決定正確構造與層序，再有限調形，不再重複單束微調。
- **恢復：** [兩束共同根](experiments/two-locks-ab/NOTES.md)、[凸度與視角](experiments/profile-convexity/NOTES.md)、[閉合底側](experiments/closed-profile/NOTES.md)、[髮流](experiments/reference-flow/NOTES.md)、[分束](experiments/separate-clumps/NOTES.md)、[根半徑](experiments/root-radius/NOTES.md)、[沿面根段](experiments/surface-root/NOTES.md)、[完整長束](experiments/whole-clump-study/NOTES.md)、[閉合截面](experiments/closed-hair-sections/NOTES.md)、[可見弧度](experiments/visible-hair-curves/NOTES.md)、[切線](experiments/hair-tangent-study/NOTES.md)。

### F3｜連續髮殼、分界谷與覆蓋量
**來源：** [UCBUGG Front Hair](https://www.ucbugg.com/labs/modeling/polygon-hair-modeling)、[Soni Part5 文字](https://design.tutsplus.com/tutorials/female-character-modeling-in-blender-part-5--cms-21211)、[dskjal 尖瀏海圖解](https://dskjal.com/blender/anime-hair-from-sphere)、[六色前髮](https://note.com/rikuhayasaka/n/n0ca6ed441394)。

- **適用：** 連續前髮面上形成分界、末端分束；規則垂下瀏海與斜向交疊尖髮要分開選法。
- **狀態：局部方法已驗證／造型未通過。** 共用根面避免完全分離；谷更可讀；尖端厚度權重有效。但矩形底接長齒仍是板片，半球髮殼仍像帽簾，後延遮蓋量變成側板。
- **戒條：** 停止在矩形叉片加細節；覆蓋髮根不等於髮根結構成立。
- **下一步：** 轉回主量塊與層序（F1），不要重新調同一片的厚度。
- **恢復：** [連續擠出](experiments/base-extrusion/NOTES.md)、[分界谷](experiments/boundary-valley/NOTES.md)、[球殼瀏海](experiments/spiky-shell-study/NOTES.md)、[覆蓋研究](experiments/overlap-margin-research/NOTES.md)、[覆蓋試驗](experiments/hair-overlap-margin/NOTES.md)。


F3 來源適用補充（研究未實作）：[dskjal 後半三中間圖](experiments/spiky-shell-study/NOTES.md)本輪補實看，既有主束側面兩縱線→頂視移谷側線→正面次尖；前提是主束與原谷已存在，不能據此猜原圖遮擋根或重做規則球殼。沒有新模型／渲染，不新增已驗技能。

### F4｜原生 Elastic Snake：根遮罩機制，不是完成髮束
**來源：** [Blender 2.92](https://www.blender.org/download/releases/2-92/) 的 [Elastic Snake 官方影片](https://www.blender.org/wp-content/uploads/2021/02/sculpt_snake-chopped.mp4) 離散影格；[Grab 4.3 手冊](https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/grab.html) 正文。遮罩手冊僅讀到搜尋節錄，直接頁面402，不能稱全文已讀。

- **適用：** 在既有有厚度草模上，測大範圍延伸是否牽動根部。
- **方法已驗證（限定本小樣）：** Blender4.3.2 原生 GUI `brush_stroke`；`SNAKE_HOOK`＋`ELASTIC`，不是 GRAB／ELASTIC_DEFORM。相同41事件、起始網格與筆刷，A未遮罩根被拖走；B全遮罩根不動但過渡折；C加寬且平滑過渡，折點較弱。
- **造型未通過：** 尚圓鈍，未有原圖尖端／層次；體積仍約比基準增加26.2%，不宣稱保體積。C同改寬度與函數，不能獨歸因其一。
- **戒條：** 不用自己的頂點移動偽稱原生筆刷；不要再在背景錯誤sculpt context重跑至崩潰；不把 `Grab Silhouette` 解釋為體積守恆。
- **下一步：** 尖端與主束分層的相近作者實作，不是繼續把同一球塊拉成勾。
- **恢復：** [Grab研究](experiments/grab-main-mass-research/NOTES.md)、[實看示範](experiments/grab-visible-demo-research/NOTES.md)、[根遮罩完整記錄](experiments/elastic-snake-root-mask/NOTES.md)。原實驗曾保存 baseline／A／B／C、腳本、數據及對照板；本公開版已附精選對照板，但未包含模型、原生重播腳本與量測資料。重播必須有可用 GUI；渲染此build需關閉不支援的去噪。

### F5｜修銳末端、局部拉束與彈性拖拉不是同一方法
**研究未實作。** [本輪方法比較](experiments/hair-tip-method-research/NOTES.md)實看 [moco GroomSpike 複試](https://mononoco.com/?p=13894)四張單幀 GIF，並完整讀 [Blender 4.3 Snake Hook](https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/snake_hook.html) 與 [Pinch](https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/pinch.html) 正文。

- **新增理解：** GroomSpike 修整既有鈍末端、Pinch 向筆刷中心收攏、Radius Falloff 局部拉束及 Elastic 整體彈性變形，各自任務不同。不能將 ZBrush 操作直接換成自製 Blender 公式。
- **適用限制：** 靜態前後圖不提供完整筆觸；細尖端也不等於目標的寬肩、彎曲側緣與分層。Toha 短尖髮只讀章節，影片黑畫面，未看操作；Cain 日文舊文只讀索引保留正文，原站已關閉。
- **當時提出的受控試驗（後續已執行，見 F6）：** 已具寬肩厚度的單束草模上固定根遮罩、網格、視窗及筆觸，只比 Elastic 與 Radius Falloff。先不加 Dyntopo／Remesh／Pinch／平滑等變數。細針、回鉤或錯誤主量仍判失敗，不整合人物。
- **本輪無新模型、無新渲染。** 研究理解不能宣稱造型進步。

F5補充回做：[原生Pinch局部練習](experiments/mass-layer-separation/NOTES.md)已實作。Soni步29–30文字與兩靜圖重讀實看；隔離Blender原生Pinch，不複製作者筆觸。正視收尖但斜／端視成薄鰭，B失敗不採用；不疊筆畫或升格為掌握收尖。

F5機制補充：[固定Z平面對照](experiments/pinch-tip-planes/NOTES.md)實讀4.3.2官方pinch.cc與calc_brush_plane，原AREA逐點重播一致；只改Z仍成薄鰭。否證固定法線足以修正本例，不證明筆畫方向是唯一原因。停止掃軸／強度，需作者可見操作證據；非造型進步。


F5收尖選法復習：[完整截面收尖](experiments/row-crosssection-taper/NOTES.md)實讀MOTOMODEL作者橫列／拓撲限制說明，未安裝插件。新規則筒以完整橫列固定長度收尖，局部沒有Pinch薄鰭；仍是對稱通用小樣，不符合原圖偏斜層疊髮束。二次衰減與焊點是自製適配，不是新收尖原理、插件實測或角色改善。

### F6｜局部拉伸較少牽動寬肩，但會形成細頸
**方法局部驗證，造型未通過。** [本輪實驗與四向圖](experiments/local-snake-falloff/NOTES.md)重讀 [Blender 4.3 Snake Hook](https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/snake_hook.html)，在新連續寬肩草模上比較原生模式，並非仿製 GroomSpike。

- **受控方法：** 同一網格、根遮罩、41事件、125px筆刷與視窗，只改 Elastic／Radius Falloff。後續D只縮短局部模式筆觸行程，不在C上疊筆。
- **限定結果：** Elastic肩部平均位移約0.11415，局部模式約0.0001603；全遮罩根皆0。局部模式出現細頸，半行程較弱但末端仍鈍；這些小樣單位不是角色毫米，也非角色還原分數。
- **失敗與限制：** 不保體積，沒有根流或分層；自訂草模的厚度與後側仍是假設。不得以封閉網格或原生操作成功稱造型通過。
- **停止／下一步：** 不連續微調此葉形束的行程／半徑。轉向相近作者主髮量、寬肩與交疊的可見建構過程；找不到逐步證據時明說。

### F7｜短寬尖束先控制主要面，表面加束不是主量的替代
**研究未實作。** [來源與觀看限度](experiments/hair-mass-overlap-research/NOTES.md)實讀 [Teng Chia 第99帖](https://www.zbrushcentral.com/t/dragonball-sculpt-i-ssj-goku-ii-freeza/205120/99)，實看普通悟空黑尖髮前後線框 WIP04、黑髮半成品 WIP05、SSJ 灰模，並比較 [Pablo Muñoz Gómez 長捲髮](https://www.pablander.academy/newsletter/stylised-sculpted-hair)七張階段靜圖。

- **新理解：** 短寬尖束可先以少量控制面建立折轉與尖端，再保形密化；長捲髮的表面 CurveTube 是主量與流向成立後的附加，不可拿來替代主量。
- **證據邊界：** 作者原詞為 Tessellate modifier，不是 Triangulate；該帖未說先存 Morph Target。線框與階段圖不是逐步操作影片，仍未看到髮根交疊／焊接的充分近圖。
- **當時提出的有限測試（後續已執行，見 F8）：** 只做一個可見寬尖主束的連續低控制籠，比較保形密化與平滑細分是否改剪影。先查 Blender 對應操作，不直接宣稱 Simple 與作者原工具等價；主形未成立前不加第二束。
- **限制：** 未有新模型／渲染，不能把「先前平滑方法可能妨礙面與尖端控制」的工作假設當已證明原因。根流和整體交疊仍待學。


F7主量分區限制補充（研究未實作）：[Hair Tubes 來源審查](experiments/hair-mass-overlap-research/NOTES.md)全文及PDF第3／4頁實看，區分已設計大束的分區與子束收尖；星形輸入仍需人工分區。共同前層表面只是待驗假設，長條髮片例不提供本角色短尖根造型答案；不重試缺接收面的投影，先找短尖髮中間建構步驟。無新模型／圖。

### F8｜先定尖形，再分開決定加密和平滑
**方法局部驗證，造型未通過。** [控制籠實驗與四向圖](experiments/spike-control-cage/NOTES.md)重讀 Teng Chia 尖髮方法、實看悟空線框，並讀 [Blender 4.3 Subdivision Surface](https://docs.blender.org/manual/en/4.3/modeling/modifiers/generate/subdivision_surface.html) 的 Simple、Catmull–Clark、crease 與支撐邊說明。

- **受控方法：** 新連續21點控制籠，以原圖最高可見主尖束外緣作低精度採樣；深度、根截面與遮擋側標假設。比較原籠、Simple三級、Catmull三級；D只在C的尖端四邊加crease1。固定相機尺度及平面著色，未加入第二束。
- **結果：** Simple保留尖端與主量；Catmull縮小主量且尖端後退；尖端crease可恢復尖端，不能補回整束寬度。A/B仍過稜角、底部截斷，D仍過窄，不能稱符合原圖。
- **限制：** Simple對非共面四邊面並非完全保留原三角化表面；本小樣單向頂點距離最大約0.005682，並非完整Hausdorff量測。Blender Simple不是已證明等價的3ds Max Tessellate，亦非Triangulate。
- **下一步：** 研究有依據的支撐面／邊線，保寬面並控制曲率，避免全邊硬折；主束未成立前不加第二束，髮根交疊仍未解。

### F9｜支撐線方向保截面，距離控制硬稜
**局部方法驗證，造型未通過；本地待同步。** [支撐線實驗](experiments/spike-support-edges/NOTES.md)實讀 [Blender4.3 Subdivision Surface](https://docs.blender.org/manual/en/4.3/modeling/modifiers/generate/subdivision_surface.html)支撐環線正文與三立方體原圖；這是一般曲面方法適配，不冒稱作者尖髮原檔。

- **方法：** 回做前輪D，原角、尖端crease與相機不變，沿每圈截面插點連成長向支撐線；B貼近稜線10%/90%，C僅放寬至30%/70%。
- **所學：** 支撐線方向能限制截面圓縮；靠近保稜強，移開過渡柔。A到B同改拓撲密度，不宣稱單一權重因果。
- **失敗：** 寬面增加不是造型驗收；底部仍圓帽狀，深度與隱藏根仍是假設，未解整體髮流。
- **恢復／停止：** A重做體積與前輪D一致，三模型可冷開；不再連續微調百分比。下一步找可見寬面弧度與面朝向建構證據，未成立前不加第二束。

### F10｜截面曲率、收尖與紋理分開診斷（研究未實作）

實看 stjun 三張作者尖束／截面圖及 UmityStudio 四張截口圖；讀 yugaki 原生曲線建構。單一拱面是主量候選，多峰谷截面產生沿程細溝，不拿紋理救主形。Sharp截面不等於髮端夠尖；閉截面不等於根端封口。既有拱面環實驗已失敗，下一次須以原生截面控制柄與傾斜分開驗證，不再重複支撐距離調參。無新模型／渲染。[來源、限制與預定最小試驗](experiments/spike-profile-curvature-research/NOTES.md)。

### F11｜先隔離中央切線，再測截面傾斜

**來源：** [stjun單拱髮束](https://stjun.hatenablog.com/entry/2022/02/27/190000)、[Blender4.3截面幾何](https://docs.blender.org/manual/en/4.3/modeling/curves/properties/geometry.html)、[Bézier控制柄](https://docs.blender.org/manual/en/4.3/modeling/curves/structure.html)。本輪重讀作者3.1–3.3及單拱靜圖，官方兩頁由雲端瀏覽器讀正文；未看嵌入影片。

- **局部驗證：** 同導向、半徑、相機，只將中央Vector柄改共線Aligned，中央切線68.19°→0°；正／斜面轉折較連續，不等於整束無稜線。
- **適用／限制：** 大塊風格化髮束的可編輯單拱面。其餘截面角仍Vector；原圖遮擋根和深度是假設，根部平切未接頭皮。
- **失敗戒條：** 初始截面寬面朝側面，保留失敗批次，再統一基準tilt90°。C另加20°只證明朝向變化，沒有更像原圖證據；不能拿Tilt冒充曲率修正。
- **下一步：** 橫向帶狀明暗尚未隔離原因；先固定B截面／導向，研究半徑插值，不能同改導向和半徑。
- **恢復：** [三變體四向渲染、前版對照、來源與限制](experiments/bevel-profile-handles/NOTES.md)。原生模型及失敗包另存，公開庫不含ZIP。

### F12｜橫帶診斷：半徑插值與平滑著色分開查
**來源實讀：** [Blender4.3 Active Spline](https://docs.blender.org/manual/en/4.3/modeling/curves/properties/active_spline.html) 的 Radius／Tilt 插值、Smooth；[Structure](https://docs.blender.org/manual/en/4.3/modeling/curves/structure.html) 的控制柄。沿用前輪作者單拱方法，本輪未重新觀看作者影片。

- **局部證據：** 截面、導向、半徑控制值、Tilt、光線不改，只把LINEAR換CARDINAL；根部接點表面折向5.30°→0.40°，真渲橫帶減弱。
- **代價與戒條：** 半徑過衝約1.29%；靠尖端5.41°→5.50°沒有改善。不可宣稱全束平順、單調或原圖相似度提升；不可用加細分／改光線掩飾，也不能暗改半徑補償單變數實驗。
- **適用與未知：** 原生Curve＋Bevel的局部橫帶隔離。切線同向不等於曲率或段參數速度一致；下一步才隔離近尖端導向與半徑沿弧長變化。根流仍未整合，不新增第二束。
- **恢復：** [四向A/B、等比例原圖、數值與限制](experiments/curve-radius-band-diagnostic/NOTES.md)。完整模型另存私人備份；不替換iteration04。

### F13｜同向不是同速度：隔離近尖端收束折轉
**來源實讀：** [Shene 的 Bézier 端點導數與 C1 接合](https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html)，Blender 4.3.2 curve.cc 半徑取樣與 key.cc CARDINAL 權重（詳見實驗）。數學教材與原生實作診斷，不冒稱新尖髮作者示範。

- **方法已驗證（限定）：** 固定平面導向與截面、CARDINAL半徑，凍結AUTO柄，僅等長第4節點一個出發柄。指定中央表面線折角32採樣5.50°→0.58°、128採樣5.28°→0.14°，解析極限5.21°→0°。
- **適用限制：** 相同段參數區間的同向等長柄支持一階導數相同；不能推廣成所有掃掠位置均光順、曲率連續或髮型更像。
- **失敗戒條：** 曲率仍不連續，1.29%半徑過衝仍在；不要用更多細分或持續微調柄長冒充造型進步。原圖可見差異很小，未整合人物。
- **下一步／停止：** 停止此孤立束的柄長微調，轉查作者主束根部延入主髮量及層序的可見證據；無新依據不增束。
- **恢復：** [速度連續性診斷](experiments/curve-speed-continuity/NOTES.md)。前B和iteration04保留；私有包含獨立baseline與核對腳本，公開僅筆記/兩板。

### F14｜底量覆蓋、前後遮擋、根部接合要分開驗證
**研究未實作。** [完整閱讀與限制](experiments/hair-root-layering-research/NOTES.md)實讀 Soni Kumari [悟空 Part1 第27–39步](https://design.tutsplus.com/tutorials/creating-dragon-balls-goku-in-z-brush-and-maya-part-1--cms-33816)，實看A28/32/34/36/38/39六張靜圖，未看影片或根剖面。

- **新增證據：** 先建立髮基底，再鋪前束、後加上部束；前束遮擋上束下段，背面半成品仍露基底。比完成前視／線框多了分階段放置證據。
- **適用條件：** 用於區分短尖髮的覆蓋底量與突出束；不能把這些圖當固定角色根深／根曲率的真值。
- **推論而非作者原話：** 底量不漏皮膚、前後遮擋成立、側斜根部不懸浮，是三個不同測試；前兩項成立不能證明焊接或融合。
- **失敗戒條：** 不再平移兩束猜根深，不增加束數遮掩懸浮，不從完成前視宣稱側面通過；原圖上方白楔和下方暗交界不一律開洞。
- **回查後撤回重複試驗：** [既有四向關底量診斷](experiments/diagonal-clump-study/NOTES.md)已證明消楔片卻露頭皮；換成前弧場景仍無新問題，不再重做。
- **下一步（未執行）：** 以舊診斷分列覆蓋區、真白縫及前束遮擋區，對照新來源分層次序；取得根接觸近側／操作證據後才提一個可見過渡改動，先列唯一新假說及舊實驗無法回答之處。
- **保存範圍：** 本輪僅文字，無新模型、渲染或教材附圖；既有基線不變。

**12:06來源篩選補充（仍未實作）：** [實讀圖文與適用界線](experiments/hair-root-contact-source-screen/NOTES.md)。Good Smile 官方前髮四張圖支持正側厚度／位置分查及不同束寬，但浮離頭部的中間球不是完成根接觸；Adam Benton PDF 的厚度曲線控制個別髮絲，不能拿來把實心寬束根縮成細針。兩者都未提供本案寬根接合依據。下一個來源需同時看見底量、可追到根端的近側束、可比的塑形前後，以及接觸和真正空隙；不以標題相近就採用。

### F15｜根彎入主量與整束平移不同；接觸不等於自然過渡

**局部實作，造型未通過。** [實驗與真實四向圖](experiments/root-entry-direction/NOTES.md)。實讀 James Hyun [Hair & Groom System](https://www.therookies.co/blog/breakdowns/complete-workflow-for-creating-a-stylized-3d-female-action-character)與兩張近側構造靜圖；只適配長髮作者的入根方向，非照搬髮型、非看逐筆影片。

- **新方法：** 保留主量，將指定根端彎向內部；不是整束前後平移。支承橢球僅測試治具，不是完成角色髮底或隱藏深度真值。
- **限定結果：** B側面直切帽不再浮離，根環取樣埋入治具；但正斜視根下段圓鼓、右交界仍有稜。接觸成立不等於完成自然根流。
- **失敗戒條：** MINIMUM會把根方向變更傳成上段截面旋轉；Z_UP又可扭折。最終包含一次相位補償，z>0.4評估殘差0.000525，不宣稱嚴格單變量或上段完全不變。失敗原樣保留。
- **下一步：** 找主量與根上表面的平面/曲率方向處理，分辨層次與突兀階差；不繼續掃深度/Tilt或加束堵縫。iteration04不變；公開只附筆記與2板，模型腳本另存私人備份。

**F15補充：根端收束負結果（13:06）。** [單一半徑欄位試驗](experiments/root-taper-scope/NOTES.md)重新讀看同作者正文與兩靜圖，把未測的收端原則適配成首點radius 1→0.5；不是Pinch重播、作者比例或原圖測量。B仍嵌入治具，卻更呈水滴/葫蘆且肩稜未解，不採用。CARDINAL使z>.5表面仍位移0.011306（約2.26px），單輸入不等於空間只動根。停止掃0.4/0.6、換插值掩蓋鼓面或加小束堵縫；下一步找寬厚分開與兩側主面方向的作者處理，而不是繼續縮根。

### F16｜曲線定束之後，表面塑形仍需目標面向

**局部實作，造型未通過。** [來源、原生重播與四向實圖](experiments/root-surface-flatten/NOTES.md)。實讀Maria Moreno流程並看3張階段圖、Pablo Muñoz Gómez主量/Surface Blocking文字與2圖；支持曲線轉幾何後處理面形，未見Hpolish逐筆操作。Flatten 3.6全文、4.3 Multiplane搜尋回傳正文及本機4.3.2 RNA的版本/讀取限制詳見NOTES。

- **適配與限制：** Blender原生Flatten單次前視筆畫，不是Hpolish等效重播。共同轉網格的A/B保留主量治具；區域平面與上段遮罩是本輪控制假設，不是作者參數。
- **限定結果：** 119點改動，上段z>0.4零位移；四向仍見寬鼓與硬接界，B不採用。它只支持可局部塑面，不支持自然銜接已學會。
- **失敗戒條：** Flatten依筆下平均平面工作，不會自動貼合/焊接另一物件；不能直接提高強度重刷或把細溝當髮流。
- **下一步：** 先取得寬根目標大面轉向與保留分層/連續面之依據，對比連續主量的實際作者操作；不再同機制掃參數。曲線基線和iteration04保持不動。

### F17｜先分負形、遮擋與面內轉折，再選塑面方法

**研究與原圖標註，未建模。** [六處判讀與下一小樣範圍](experiments/hair-boundary-design/NOTES.md)。實讀Scott Spencer Wiley公開節錄p25–27並看Fig1.31–1.37，區分連續獅鬃面凸脊/凹谷；實讀Alina/Adaline Jinx的Blocking/Hair與3圖，區分主量及獨立束遮擋。不是本案逐筆示範，也不把所有硬邊當待消接縫。

- **固定原圖判讀：** 1/4/5有前後搭疊依據，3為背景白色負形，2/6為面內流向線索；後者凸凹符號與高度仍未知，暗線不能逐條當槽。
- **修正驗收目標：** 前弧本來遮住高束下段，不應用消掉全部分層線驗收；停止裸露接球根微調。可見外緣、白隙和前弧遮擋先保留。
- **下一小樣：** 高束可見上段寬面，一條主轉向、兩側寬面；先定目標面向再查原生工具，不用細溝假裝大面改變。側斜仍查管狀鼓包/硬斷台，背面僅檢查影響，不宣稱隱藏根更準。
- **邊界：** 新圖是授權原圖同尺度標註，不是新渲染或已解造型；iteration04及前輪失敗不動。

### F18｜主脊位置改面向，不等於寬面曲率成立

**局部機制驗證，造型未通過。** [四向與原圖比較](experiments/visible-plane-balance/NOTES.md)。重讀六色截面第4/5節及截面實圖、讀Blender4.3 Move與Orientation正文。主脊可偏心是本輪有據適配，0.35不是作者配方或原圖量測值。

- **方法：** 沿用舊61點控制籠，固定深度/支撐距離/外緣/根環/尖端及前弧鄰束，只上四環20個內點用原生Edit Mode Global X移動，主脊0.50→0.35。兩側面寬和面向改變，沒有刻細溝。
- **結果與戒條：** B仍偏硬、不採用；固定外緣控制點不代表細分渲染剪影固定，實際最大差1px。舊上下文仍有側面/根部缺陷，不因遮住下段就稱根修好。
- **失敗保留：** 第一稿誤動隱藏根環；修正範圍後重渲，不把4px→1px當審美改善。模型與失敗初稿另私人保存。
- **停止／下一問：** 不掃0.4/0.3等主脊比例；先找作者怎樣保寬面方向而建立連續轉折帶，回查支撐線/截面舊失敗後才設下一試驗。iteration04不動。

### F19｜倒角弧面與細分最終曲率分開驗證

**局部負結果。** [本輪四向與原圖對照](experiments/ridge-transition-band/NOTES.md)。實讀Blender4.3 Bevel Edges全文及單段/四段兩張官方圖；六色及Maria只回查已讀筆記，未本輪重看。官方方塊工具示意不是相近髮型實作。

- **方法差別：** Bezier共線柄控制掃掠截面切線；本輪在既有多邊形籠三條上脊邊做Offset .04、4段、Profile .5原生Bevel，再保留Catmull三級。數字為一次試驗值，非作者髮型配方。
- **結果：** 新弧面密度在本例強化窄硬亮帶，未形成寬柔轉折，B不採用。不能推成所有Bevel都變硬。邊界控制點保留仍有1px投影差，不能以此宣稱原圖精準。
- **停止：** 不掃倒角寬度/段數，也不退回支撐距離微調。先對照Bezier有效切線例與倒角負例，找作者對整個可見截面寬轉折及沿長度曲率分配的操作證據。
- **保留：** 前弧/鄰束上下文固定但仍有舊缺陷；沒有修好根、主量或厚度，不整合人物，iteration04不動。

### F20｜先看評估後的轉向分布，不把控制籠圓角當柔和曲面
**既有幾何診斷，無新造型。** [法線四向重渲與截面](experiments/ridge-curvature-diagnostic/NOTES.md)實讀[OpenSubdiv曲面概念](https://opensubdiv.org/docs/subdivision_surfaces.html)與[建模注意](https://opensubdiv.org/docs/mod_notes.html)正文；少跨度圖片取得失敗，沒有看圖或影片。舊六色/Maria僅回讀紀錄。

- **方法：** 原A/B幾何不動，同細分三級評估，在兩個可見高度取實際表面及投影法線；另四級檢查趨勢，不當新模型或精確微分曲率。
- **限定發現：** B的共同轉向窗口比A窄且峰更凸，符合窄硬亮帶；兩者均Smooth、無custom normals，排除忘記平滑這項簡單原因。密集邊與結果一致，但未隔離各拓撲因素，不稱唯一因果或所有倒角必然變硬。
- **決策：** 保留A、不採B，停止掃倒角/主脊參數。先定完整可見截面的寬面與轉向帶假設，再找少跨度構造證據；不可從診斷數字生成無據推點配方。
- **限制：** 原圖沒有曲率真值；兩截面與新法線重渲不是相似度分數，也不證明整束已懂。新圖非舊渲染冒成果，模型本身未改善。

### F21｜回做早期完整拱面截面，確認新上下文的適用性
**早期方法恢復，不是新發明。** [修後導向與前弧上下文回測](experiments/whole-profile-retest/NOTES.md)重新讀stjun 3.1–3.3並實看單拱截面原圖；實讀Blender 4.3 Handle Types，沒有看嵌入影片，也沒有公開第三方圖。

- **方法：** 保留修後等速縱向導向、半徑與共同前弧／鄰束；只比較凸側中央兩柄Vector與Aligned。共線代表切線方向連續，非曲率C2保證。
- **回測結果：** B在正／斜視仍重現較連續完整拱面，固定前視480px、alpha閾值128的主束輪廓無差；不推論所有視角或3D相同。確認保存的早期方法可恢復並帶入新上下文，不重複算作新發現。
- **戒條：** 側面平根帽與舊上下文仍差，背側角仍在；B只作連續截面工具基線，不取代iteration04，不加細槽或整頭複製。不得把不同表示法的倒角案例當單變因排名。
- **下一問題：** 如何沿長度改變寬面朝向與不等寬分層而不擾外緣、產生橫帶。原生A/B冷讀已驗；異地解壓完整重建未驗，公開庫不含所需原生模型／腳本。

### F22｜根邊界與自由尖端分工，不能靠前視藏住失敗
[前弧根流局部比較](experiments/forelock-root-flow/NOTES.md)：實讀UCBUGG Front Hair／Side Hair／Notes，實看picture11、17、20；Umity Split Bangs僅讀文字、未看圖。長髮方法只適配表面接續原則，不照抄隱藏根形。

- **方法差異：** 舊A首尾皆匯合成尖點；B改有限寬表面根邊界並後延，C再彎向上／後。根端座標、厚度與深度都是測試假設，非原圖量測；這是構造比較，不是單變因實驗。
- **實驗結果：** 正面去右尖不代表附著成功。B成懸板；C側面外翻耳片、背面穿出高束；加厚也使左下尖端鈍化。兩者失敗保留，不取代iteration04或較好基線。
- **戒條與適用限制：** 貼形需要可信支承面；沒有前額／鄰束接收面時不繼續猜隱藏顱深，不縮根、添束堵洞或以正視遮住失敗。
- **下一問題：** 從可見重疊邊界建立局部接收情境，再比較連續片與獨立髮束的接續方式。私有原生輸入／腳本已保存；公開板可檢查結果，但不足以獨立完整重建。

### F23｜接收面不能從幾何接觸升格為造型證據
[前弧支承研究](experiments/forelock-support-research/NOTES.md)實讀 Reallusion CC Asset Developer Guide 第17頁並看三圖；Umity 馬尾教學 Part1 步驟1–7及Part2基底選擇段、前9圖實看，沒有影片或外掛操作。本輪無新模型／渲染。

- **方法差異：** 頭表面、可見髮底／主量、不可見生成底與前弧的角色不同。作者由既有頭面建立底，再調髮際與分層；薄髮片及馬尾案例只借接收面原則，不當實心尖束配方。
- **新核對：** iteration04髮底來自參數環與徑向射線外推，不是已驗證額部面複製。接上它可證幾何接觸，不證原圖髮際／量感正確。
- **舊失敗戒條：** supported-hair-root已做Mask Extract，卻因自造支承與遮擋關係錯誤失敗。抽面、膨脹、再猜根不是新方法；不重演隱藏支承面只看伸出片。
- **下一步與停止條件：** 先核對隔離前弧／鄰束與04可見額部能否用共同剛性變換＋等比尺度註冊；缺可靠基準即停止接根。如成立再顯示全部接收關係做四向診斷，不以cap當治具強吸所有根。仍未學會自然根部，不改較好基線。

### F24｜共同前視換算，不等於三維接根註冊
**既有幾何的新診斷，沒有新造型。** [本輪證據與四向實渲](experiments/forelock-registration-audit/NOTES.md)實讀[Blender4.3正交相機](https://docs.blender.org/manual/en/4.3/render/cameras.html)的Orthographic／Scale／Shift段；web回402後公開HTTP取得全文，未看影片。回查自製原腳本，不冒稱作者雕刻示範。

- **可重用：** 追原圖hash、像素原點、單位與歷史object平移，再用共同等比＋平移匯入；不逐束或逐軸拉伸。本案舊人工頰顎153px/unit、局部100px/unit可推s=100/153、tx=5/153、tz=2.72+213/153，這仍不是額部三維校準。
- **限定結果：** 前視投影可追溯，Y深度無約束；Y0只作原點示範。沿Y平移1單位的前視變化僅浮點殘差，不是移動建議。新四向板顯示平帽／缺接收連續性，但不能據此量出真實根深或改深方向。
- **失敗戒條：** 不把舊04髮尖當新局部束對準真值；頭部可見頰顎暫保不等於髮際已驗證。不掃ty、不補中央束、不猜隱藏顱深。缺額部／接收面地標與深度觀測就停止接根，沒有基線升級。
- **恢復教訓：** 匯入全部物件後update依賴圖再取matrix_world，曲線的隱藏bevel profile也必須連入scene。冷讀共同變換殘差<5e−7、頭/cap差0，只證保存保真，不證造型通過。模型腳本另私存，公開兩板不能獨立重建。
- **下一步：** 查有完整頭部上下文的作者案例，研究可見髮際／中央瀏海如何標識接收面；先分可見約束與遮擋假設，沒有新空間證據只能做獨立方法練習。

### F25｜原圖吻合與未知視角可用性，分開驗收
**研究／待執行規格，無新模型或渲染。** [本輪來源記錄](experiments/oblique-reference-limits/NOTES.md)實讀[Jasper Ritsema第一人稱訪談](https://80.lv/articles/stylized-character-from-2d-to-3d)Matching／Face／Hair，實看原畫、Sphere與Refining blockout兩階段、前後斜線框及UV圖；實讀[Mido Lai](https://80.lv/articles/character-production-workflow-overview)Blockout／Hair，實看初二階段多視圖。沒有看逐筆影片，Timeline只讀文字。

- **新增理解：** 不可量出原圖唯一深度，不代表不能提出可撤回的三維設計。作者未知髮背以合理性設計；它是設計而非還原真值。短尖髮與頭盔捲髮方法不同，只適配保存比較相機、主量優先與驗收分工，不移植其FOV或束身份。
- **兩套驗收：** 固定前視判原圖可見尖端／負形／前弧遮擋；其他角度判自交、浮端、薄片、穿皮與髮流。原圖非正側不得跨圖硬配同名束或疊像素求唯一深度。後者通過也不等於前者吻合。
- **有界下一步：** [H1規格](experiments/oblique-reference-limits/VALIDATION_SPEC.md)先從現有後邊界及長向切線做一次首命中診斷；只有局部代理髮底量命中才生成一個局部接續候選。不移整束Y、不加束遮錯、不放大cap、不掃方向或深度。
- **停止條款：** 無邊界／切線、先撞皮膚或鄰束、需穿整個主量時立即停。即使候選四向暫過，也只能叫此代理上下文的局部設計假設，不升04或宣稱原圖根深已知。H1目前未執行，沒有通過結果。

- **18:36前提更正／撤回：** [輸入血緣核對](experiments/forelock-support-h1/NOTES.md)顯示audit B仍是舊雙尖前弧；B-aligned-arch不等於B-finite-root-strip。H1所需有限後邊界不在指定輸入，因此未射線／延伸，不得寫成接觸失敗或新發現雙尖。原H1不得原樣重排。
- **修正戒條：** 先列分支SHA、實際物件與可操作控制面邊界，再寫變形規格；A/B/C不能跨實驗當全域版本名。下一步仍須新的有向根截面／後緣方法依據；不得暗換已失敗B/C直接重調。這是流程修正，不是造型進步。

### F26｜支持面貼合與自由尖髮不可整束混用
**局部失敗，不採用。** [單尖面片實驗](experiments/forelock-surface-strip/NOTES.md)實讀UCBUGG Front Hair與Notes，新增實看13/16/19圖，重看17/20。作者面片先近額面，Closest貼合後分束、加厚，再以後邊接後髮；長瀏海方法適配短尖髮須另驗。

- **實作：** 新26點20面，有限根邊界與單個遠端尖點；原生Shrinkwrap後Subdivision及Solidify。不是重用失敗B/C或延續已撤回H1。
- **失敗：** Y=-1遠工作面且整束Closest投影，把前弧壓成小額片；X/Z最大移動.527111，根長.154254→.062158。數字不是品質分數；沒有自然接根或原圖進步。
- **戒條：** 作者近表面前提未滿足，不能說作者方法失效。支持區與自由輪廓須分工；頭表面不是髮帽支持量。不要再整束投影或掃深度/角度。
- **下一問題：** 先辨識可信支持區與邊界，再從該邊界建立自由尖髮；可見X/Z與側弧仍待驗。04未改，未知深度未解。

### F27｜可見高位接點不等於直接貼頭根
**適用性門檻實測；沒有新髮形。** [局部支承診斷](experiments/forelock-support-gate/NOTES.md)重讀UCBUGG並新增實看picture14：作者貼額後會移高／縮放，再分束加厚與後緣接後髮；成品可見接點不必等於初始支持面。另實讀Blender4.3官方Shrinkwrap的Vertex Group、Nearest、Project段；web402後直接下載取得正文。

- **實測：** 只用ROOT_ONLY群沿Y做原生PROJECT。選定影像接點Z3.968366–4.092549高於04頭面maxZ3.869168，5條射線均不命中，群內位移0。群外不動不能與投影成功混稱。
- **限制：** 證明的是這條接點不能直接投到此舊頭面，不是頭部真值或自然根流已驗證。影像接點不是已確認解剖髮根；前視註冊與未知深度仍有限制。
- **戒條：** 局部選區不能創造不存在的接收面；不改用Closest硬拉低、不放大隱藏顱頂、不拿未驗證髮帽替換目標。保留04，停止自由區延伸，無新髮形。
- **下一步：** 尋找近額支持區→自由轉折→高位可見交界的作者建構證據，或貼額後移高與後髮連接的可恢復操作；不得由此猜出後延根片。兩板清楚區別前輪失敗舊渲與本輪舊幾何診斷重渲。

- **20:06補充／覆寫下一步：** 換現有主束與鄰束作接收面也各5/5未命中；UCBUGG新增picture22/23靜圖只證明區域分工，不展示隱藏根截面。延伸tab與舊餘量失敗重複，撤回未做。停止同高邊投影／Y掃描／tab延長；下一個不同問題為寬前殼與主量共同面轉向，先需具體操作或分階段幾何證據。無新模型或圖片，不新增技能卡。

- **20:36來源判讀補充：** Reimu作者正文＋三組GIF各3離散影格顯示共同上方前髮面、整組Bbone變形及另行長髮beveled-normal修飾，三者不可混稱幾何接合。Flat Modeling影片黑畫面、字幕未取得，只讀章節不能實作。下一步先取得平面變彎面／接邊的實際過程；無新模型圖、不猜包覆參數，也不全頭套半球。詳同篇F27附錄。

## 三、五官：先把尚未完成的事記清楚

- **早期五官試作／未核實：** 尚缺可核對的基底授權與五官前後檔，不列為已完成成果。
- **研究未實作：** [Julien Kaspar 頭部拓撲](https://julienkaspar.artstation.com/blog/M3LL/head-retopology-of-snow)、[Blender Studio 面部拓撲](https://studio.blender.org/training/stylized-character-workflow/5e5407ec8faf011a381510d7/)、[表情指南](https://studio.blender.org/training/stylized-character-workflow/5da0599be2e7bac4cc81bd61/)。舊學習準則（未包含）記錄查過公開內容／課綱，**不是看完整課程，也不是已練成表情**。
- **適用與下一步：** 頭髮階段穩定後，先眼球包覆、眼皮厚度、眼口環線及局部表情試驗；再做正式拓撲／Shape Keys。
- **戒條：** 不在球面換眼嘴就稱人物像；表情名稱和數量不是品質證據；正式拓撲未定前別把探索副本當綁定母版。

## 四、身體四肢：結構與變形仍待正式驗證

- **研究未實作／局部診斷：** 舊準則提及 [Armature](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/armature.html) 與 [Corrective Smooth](https://docs.blender.org/manual/en/4.2/modeling/modifiers/deform/corrective_smooth.html)。不是關節變形已驗收；保體積／平滑修正也不是拓撲與權重的替代品。
- **已確認缺口：** [袖內支撐稽核](experiments/sleeve-support-audit/NOTES.md)證實04的指定右前臂物件從 local x≈.95封口，沒有延伸到袖內；不是局部抽取誤刪。後續支撐代理是從可見前臂推延的假設，不是完成上臂解剖。
- **適用與下一步：** 輪到四肢時先建立完整肩臂／掌指／腿足連續體，再分形體、拓撲、關節中心、權重檢查。小角度與大彎曲都測；輸出GLB再匯入需另驗。
- **戒條：** 不能刪人體取得無穿透；不能靠加Smooth宣稱手腕修好；個別剖面無相交不能稱全體動作通過。

## 五、穿著：存檔，不越過目前頭髮階段

### C1｜衣殼、回折、層序、厚度與支撐
**來源：** [Soni Part6](https://design.tutsplus.com/tutorials/female-character-modeling-in-blender-part-6--cms-21357)、[Dita 捲袖](https://support.clo3d.com/hc/en-us/community/posts/360000423308-How-to-Roll-up-a-Sleeve?sort_by=votes)、[Style3D 折邊](https://help.style3d.com/studio/en/c4905/d2d78/19ef3/dcf1c/f3fad)、[MD 碰撞厚度](https://support.marvelousdesigner.com/hc/en-us/articles/47358430412441-FABRIC-PHYSICAL-PROPERTIES-Adjust-Collision-Thickness)。各來源實看／僅讀文字差別以原 NOTES 為準。

- **方法已驗證／造型未通過：** 去封面、生成內外壁建立真正開口；同一曲面連續回折而非相交圓環；最終三角面剖面可查局部侵入。袖子仍硬套筒／層序不明，盲薄化沒有可信餘量。
- **適用：** 服裝結構檢查，先有完整支承、厚度預算、實際層序，再加皺。
- **戒條：** 可見布厚不等於碰撞厚度；內部暗線不證明三層；沒人體的空隙不能當合體。
- **下一步（到衣物階段再做）：** 真實短翻袖層序與受力，再整合衣殼。
- **恢復：** [開口](experiments/sleeve-opening/NOTES.md)、[回折](experiments/sleeve-return/NOTES.md)、[層序假設](experiments/sleeve-layer-hypotheses/NOTES.md)、[包覆](experiments/sleeve-layer-wrap/NOTES.md)、[內貼邊](experiments/sleeve-facing-landing/NOTES.md)、[淨空](experiments/sleeve-clearance-study/NOTES.md)、[支撐衣量](experiments/supported-cloth-volume/NOTES.md)。

### C2｜先寬布面，再窄谷；禁止在錯誤圓管上疊凹凸
**來源：** [Gvaat 布褶圖解](https://gvaat.com/blog/how-to-draw-folds-in-clothing-and-fabric-a-step-by-step-tutorial/)、[Kirill Senzu](https://www.artstation.com/artwork/XgABvw)、[Ben Simonds 公開試讀頁56–57](https://nostarch.com/download/samples/Blender_ch5.pdf)、[Mongrelman 實作討論](https://polycount.com/discussion/65159/modeling-folds-wrinkles)、[Soni 軀幹截面](https://design.tutsplus.com/tutorials/female-character-modeling-in-blender-part-3--cms-20358)。2D圖解用於分析，不冒稱3D操作。

- **方法局部有效：** 支撐列控制細分轉折；沿路徑擠出截面，兩端收窄、降起伏可讓折線回到寬面。可見袖下緣擬合改善只是局部結果。
- **造型未通過：** 加深舊圓褶→補丁感；搬上峰→隆包；獨立折面仍浮雕薄板；胸腰截面第一次過鼓。擬合用點的殘差不是獨立驗證。
- **適用／下一步：** 從連續寬面建立面朝向、局部折區與受力，不是先密集皺紋。
- **恢復：** [主要褶](experiments/sleeve-primary-folds/NOTES.md)、[褶漸消](experiments/sleeve-fold-runout/NOTES.md)、[比例校準](experiments/sleeve-proportion-check/NOTES.md)、[下緣候選](experiments/sleeve-lower-contour/NOTES.md)、[上峰失敗](experiments/sleeve-upper-fold/NOTES.md)、[分面失敗](experiments/sleeve-plane-groups/NOTES.md)、[新片研究](experiments/fresh-patch-method-research/NOTES.md)、[支撐列](experiments/fresh-fold-support-loops/NOTES.md)、[折線起訖](experiments/fresh-fold-runout/NOTES.md)、[肩衣殼](experiments/shoulder-shell-extrusion/NOTES.md)、[肩形參考](experiments/shoulder-reference-fit/NOTES.md)、[胸腰截面](experiments/chest-volume-sections/NOTES.md)。

### C3｜物理與原生筆刷：測機制，不拿求解皺褶當美術成功
**來源：** [Blender Cloth Shape](https://docs.blender.org/manual/en/latest/physics/cloth/settings/shape.html)、[SideFX 布料原理](https://www.sidefx.com/docs/houdini/vellum/clothsimulation)、[Pablo Dobarro 2.91](https://code.blender.org/2020/10/cloth-sculpting-improvements-in-blender-2-91/)、[4.3.2 paint_stroke.cc](https://raw.githubusercontent.com/blender/blender/v4.3.2/source/blender/editors/sculpt_paint/paint_stroke.cc)。

- **方法已驗證：** 餘量＋端部約束產生皺；固定區左右哪些面能動；縫合鬆邊的小樣保持接合；Pose Cloth 明確9／81事件原生重播結果不同。
- **造型未通過：** 壓縮過密、固定袖口像硬環、放開後尖折、回正仍凹陷；遮罩鎖住錯形不能救回。接觸／摩擦測試未得到正確短袖。
- **戒條：** UI輸入81個路徑點不等於Blender接受81次；Pose不走一般spacing分支，不能盲套；縫合關掉仍留跨片邊不是無連接控制組；碰撞距離不是厚度保證。
- **下一步：** 等衣物階段才回到支承正確的短袖，禁止重跑相同物理參數代替形體學習。
- **恢復：** [壓縮](experiments/sleeve-compression/NOTES.md)、[固定範圍](experiments/sleeve-pin-region/NOTES.md)、[接觸](experiments/sleeve-contact/NOTES.md)、[縫合](experiments/seam-constraint-sample/NOTES.md)、[曲面接觸](experiments/curved-facing-contact/NOTES.md)、[Pose來源](experiments/pose-cloth-source-study/NOTES.md)、[事件數受控重播](experiments/pose-cloth-event-density/NOTES.md)、[回正](experiments/pose-cloth-return/NOTES.md)、[遮罩負結果](experiments/pose-cloth-mask/NOTES.md)、[支承來源稽核](experiments/supported-fold-source-review/NOTES.md)。

## 每輪讀回與恢復流程

1. 先查任務是否仍活躍；活躍就跳過，不另開補跑。讀本頁「目前位置」及最近一輪 NOTES。
2. 打開對應方法卡的失敗例與原圖；寫一句本輪要解的問題。若與停止條款重複，先找新證據，不再盲調。
3. 核對當前較佳基線、時間與hash；複製至新實驗資料夾。保留原始網格、原生筆刷設定、相機、材質、單位、來源讀看範圍。
4. 需要重播時先看每個 NOTES 的執行條件。背景渲染與 GUI sculpt 不混用；不同視窗尺寸不要盲沿用桌面座標；快取外還留冷凍網格。
5. 固定正／側／背／斜角對照；原圖等比例。記明新增鏡頭是診斷，不拿它替代同視角前後比較。未知深度標假設。
6. 記錄「實際學到／試驗失敗／仍未知／下一步」。若是研究輪，明說無新模型；失敗保留，不升級基線。

## 本索引的證據限度

依現存實驗 NOTES 與歷史技術紀錄整理；來源「已讀／實看」描述的是當時記錄，不假稱這次重新觀看59套教材。舊文頁面版本可能變動，重做須核對本機版本。早期基底、五官與未保存成果待找原檔後再補；不要用空白處猜歷史。寧夏夜市、V3 等場景由另一份歷史索引整理，不混作人物方法已學會。

### 頭部補充研究入口（研究未實作）
[下頰—下顎研究](experiments/head-cheek-research/NOTES.md)：[Anatomy For Sculptors](https://anatomy4sculptors.com/blog/forming-the-head-simple-to-complex/) 全文與咬肌／脂肪／成長比例三圖，區分骨性方向和表面頰量；[Dave Reed 公開逐字稿](https://www.skillshare.com/en/classes/advanced-character-modeling-with-nomad-sculpt/1733737655) 提示補量後 Move、輕 Smooth，但未看課程影片，無法還原落筆。適用於診斷，不把成人比例套Q版，不把舊渲染當本輪改善；下一步以局部操作示範補足驗證。


## 公開版內容邊界

固定案例為綠衣、紅圍巾、黑尖髮、空手 T pose 的 Q 版三視圖。已附使用者授權的[固定原圖](images/reference/character-three-views.png)及精選實渲／對照／分析圖；各篇文末「公開附圖」的有效連結表示實際附檔，歷史檔名不代表全數上傳。人物模型、原始建模／重播腳本與求解快取仍未納入。上述「恢復」連結導向筆記及已選圖，不代表完整模型恢復資產隨附。請先讀[復現說明](REPRODUCING.md)。

### 完整截面收尖的停止條件補充

[截面小樣及適用性回查](experiments/row-crosssection-taper/NOTES.md)：已有方向的曲線末端 radius 0 與低籠單尖點都已收束。無新的輪廓修正理由，不把已尖主束再次縮窄。是否能用取決於完整列辨識及需求，不是只看有無三角面。此次無新模型／圖、非新增技能；回到主量與前層面轉向。
