# 08:06 來源學習：整段袖管形變如何產生主褶皺

## 本輪結論
找到並真正看到了製作動作，而非只有完成圖。已在 原生 Blender UI 做出一次真實 Pose／Cloth Simulation 筆觸，但只得到輕微彎曲，沒有作者的集中褶群；因此仍未練成。四向 A/B 是失敗練習證據，不是角色改進圖。

## 已實讀與實看的第一手來源
Pablo Dobarro，Blender Developers Blog，2020-10-20：
https://code.blender.org/2020/10/cloth-sculpting-improvements-in-blender-2-91/

文章中 Cloth Deformation Target 段落說明，Boundary / Pose 工具的 Deformation Target 可設為 Cloth Simulation；文章描述可製作袖子等布褶，不必依賴碰撞。

嵌入示範影片：
https://code.blender.org/wp-content/uploads/2020/10/Simulation_Target.mp4
長 43.233333 秒、1920×1080。從作者頁已實際載入的 video 元素下載觀看；未執行作者程式、沒有登入或購買。影片只作內部學習，不放入交付。

**實際觀看範圍與方式**：0至40秒每5秒取一張影格檢視整個順序，另外23秒與32秒以1920×1080原尺寸檢視。不是連續逐幀看完，也沒有聽到或取得旁白。
- 0–15秒：平片邊界工具示範；不是本輪袖子目標。
- 20秒：平滑開口管狀網格，畫面中沒有手臂。
- 23秒：Pose工具圓圈覆蓋管右側，大致錨在管中間；設定見下一節。
- 25秒：右段彎下，壓縮轉折出現集中褶皺。
- 30秒：袖管較直，中央仍有褶皺。
- 32秒：再次可見彎曲及轉折皺褶，寬直段與窄轉折相接。
- 35秒：管段方向再變，中央留下斜向褶皺。
這些分散影格能確認前後形體與顯示設定，不能精確還原每一筆滑鼠路徑或操作鍵，也不能直接把它等同本角色翻袖。

## 看清的設定／尚缺的資料
23／32秒可讀：Pose；Deformation Target = Cloth Simulation；Deformation = Rotate/Twist；Rotation Origins = Topology；Smooth Iterations = 4；Pose IK Segments = 1；Keep Anchor Point與Connected Only勾選；Strength = .500；Radius = 498 px；Pose Origin Offset = .000。

仍未取得：網格初始分段數、尺寸、完整筆觸事件、所有隱藏進階設定、布材質參數。不能聲稱範例已證明手臂接觸、防穿透、布厚或固定T-pose下的翻袖結構。

## 方法帶來的具體新理解
前輪直接改下側餘量只能建立衣物空間，無法自動產生折線。這個示範採取的是先有整段連續寬面，再由局部旋轉／扭轉與保留錨點，讓整個轉折區在布料目標下共同變形；沒有把獨立尖條貼到表面。

下一個可重現動作應只做「空管右段彎曲一次」：先確認能在壓縮側形成轉折，再討論伸直保留折痕。不應跳到角色，也不應把未知參數寫成來源精確配方。

## 實際重現嘗試與失敗
建立新隔離測試，不載入／修改角色與先前袖子：64周向×81軸向的開口網格、長3、半徑.42。這是自己的測試解析度與尺寸，非作者資料。保存 before-stroke.blend。

test_stroke.py 使用 Blender 4.3.2 內建 Pose／Cloth Simulation，準備一筆錨定旋轉的試驗。預計從世界(1.2,-.42,0)到(1.0,-.42,-.65)，31筆取樣。這是我的重現路徑假設。

**執行條件限制**：背景模式未建立有效的互動雕刻視窗，不能視為筆觸已執行；後續改在有效的 Blender 互動視窗測試。這是上下文條件，不是造型改善。

**實際 UI 練習**：控制台建立 Pose／Cloth Simulation 筆刷後，Blender 4.3 還必須 asset_mark 並以 brush.asset_activate 啟用本地 Brush 資產；單獨指定 tool_settings.sculpt.brush 沒有出現有效筆刷標頭。啟用後畫面顯示 Source Pose Cloth test、Strength .500。統一筆刷半徑設 240 px（本畫面管長約560 px，非作者498 px的精確等比重現），停用 X 鏡像。
保存 pre-ui-stroke.blend。以真實滑鼠沿右側寬面向右下拖曳；不是公式加波形或位移頂點。

**結果**：右段略向下彎，左段大致保持；沒有看到示範中央集中折線。這是可恢復的失敗實驗。不能將滑鼠行程當作實際幾何行程。來源2.91與目前4.3、未知網格密度/比例、筆刷覆蓋範圍、拖曳事件時間與布料求解收斂都仍有差異；沒有證據判定單一根因。下一步應查清 Pose 的 cloth solver 對事件時間/步數與半徑影響，最好取得作者可重現示例，再做單因素試驗，不能隨便加大數字把它弄皺。

**驗證**：render_comparison.py 從 before-stroke 取 A、after-ui-stroke 取 B，沒有額外形變；固定同相機、同燈光、同正交尺寸輸出 front/side/back/oblique 八張。measurement 只確認筆觸確有改動，不作美感改善證據。沒有和前輪較好基線替換，也沒有把彎管接到角色。

## 其它來源的狀態
- Jan van den Hemel 作者頁 https://www.3dsecrets.com/secrets/realistic-cloth-wrinkles-and-folds-with-no-effort ：瀏覽器實開404，沒看到影片，不稱學會。
- Blender Studio 的 Sculpting Wrinkles & Folds 搜尋可讀簡介；本輪沒有看付費示範，也沒有購買。
- YouTube只取得Blender Secrets影片說明；沒有聲稱播放成功。

## 公開文字版範圍

本頁整理既有實驗筆記，未在本次公開整理中重新執行或獨立重現。原始 `.blend`、參考圖、渲染、量測 JSON 與實驗腳本未包含在此文字版；文中檔名只描述當時的證據，不是下載連結。第三方教學內容僅保留公開來源連結與閱讀／觀看範圍，未重散布圖片或程式。歷史階段與下一步以當時紀錄為準，最新方向請見根目錄索引。
