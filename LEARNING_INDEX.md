# DOTS 人物建模學習記憶：方法、失敗與恢復索引

更新：2026-10-29。這是可查閱、可重做的外部記憶，不代表模型權重自我訓練，也不保證未來會自動讀到。**每輪開工必須先讀本頁及對應 NOTES，再決定實驗。**

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
- 最新研究：[尖端修整方法比較](experiments/hair-tip-method-research/NOTES.md)，尚未實作。
- 最新工具小樣：[局部衰減與 Elastic](experiments/local-snake-falloff/NOTES.md)。尚未整合人物。
- 使用者提供的作品展示入口：[Max.0821 的 Sketchfab](https://sketchfab.com/Max.0821)。已核對公開目錄名稱及部分作品連結，詳見 [街景與寧夏歷史](history/SCENE_LEARNING_HISTORY.md)；目錄存在不等於逐件驗收。

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
- **下一個受控試驗（尚未執行）：** 已具寬肩厚度的單束草模上固定根遮罩、網格、視窗及筆觸，只比 Elastic 與 Radius Falloff。先不加 Dyntopo／Remesh／Pinch／平滑等變數。細針、回鉤或錯誤主量仍判失敗，不整合人物。
- **本輪無新模型、無新渲染。** 研究理解不能宣稱造型進步。

### F6｜局部拉伸較少牽動寬肩，但會形成細頸
**方法局部驗證，造型未通過。** [本輪實驗與四向圖](experiments/local-snake-falloff/NOTES.md)重讀 [Blender 4.3 Snake Hook](https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/snake_hook.html)，在新連續寬肩草模上比較原生模式，並非仿製 GroomSpike。

- **受控方法：** 同一網格、根遮罩、41事件、125px筆刷與視窗，只改 Elastic／Radius Falloff。後續D只縮短局部模式筆觸行程，不在C上疊筆。
- **限定結果：** Elastic肩部平均位移約0.11415，局部模式約0.0001603；全遮罩根皆0。局部模式出現細頸，半行程較弱但末端仍鈍；這些小樣單位不是角色毫米，也非角色還原分數。
- **失敗與限制：** 不保體積，沒有根流或分層；自訂草模的厚度與後側仍是假設。不得以封閉網格或原生操作成功稱造型通過。
- **停止／下一步：** 不連續微調此葉形束的行程／半徑。轉向相近作者主髮量、寬肩與交疊的可見建構過程；找不到逐步證據時明說。

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
