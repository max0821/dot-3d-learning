# 支撐形體與局部折區：來源適用性研究

2026-10-29 10:06 UTC 輪；DOTS。**這輪沒有新模型、沒有渲染成果，也未練成水平短袖。研究結果是排除兩種不充分的直接套用，並確認衣殼包覆與加皺必須分開驗收。**

## 先讀前輪，不重跑物理參數
已讀 sleeve-contact/NOTES.md 與 curved-facing-contact/NOTES.md：摩擦極端值外觀差異小、接觸小樣只驗證有限機制；不再做摩擦或縫合碰撞的參數重試。pose-cloth-mask 的負結果是固定錯誤的彎管形體使回正凹口更寬；本輪不調整該管或 mask。

## 實讀、實看的來源
### 1. Pablo Dobarro／Blender Developers Blog
https://code.blender.org/2020/10/cloth-sculpting-improvements-in-blender-2-91/
實讀 Collisions、Dynamic Simulation Area 兩節；官方影片由頁面 video 元素確認並下載，只作閱讀，不執行陌生程式。
- Cloth_Collisions.mp4，34.566667 秒：看每 5 秒取樣接觸表與 5 秒原尺寸。
- Dynamic_simulation_area.mp4，44.766667 秒：看每 5 秒取樣接觸表與 5 秒原尺寸。
這是離散影格檢視，不是完整連續播放；無聲音內容或精確滑鼠事件的聲稱。

碰撞示範：白布跨在紅色球、環、方塊上，Grab 拉動整片布，布沿障礙物改變包覆。5 秒可讀 Grab、Enable Collisions 勾選、Persistent 勾選。這支持先有外置布面與障礙物再拉動的流程，但不是短袖的製作步驟。作者文中也說已進入碰撞物內的頂點不能靠該射線碰撞推出。
局部示範：球面上沿路徑產生狹長壓摺，再膨起局部皺團。5 秒可讀 Dynamic、Pinch Perpendicular，碰撞未勾。它展示筆路附近的求解範圍，不展示袖子如何承接肩部或維持手臂空間。

### 2. Roblox 官方 Sculpt detail
https://create.roblox.com/docs/art/accessories/creating/sculpting
英文原始 Markdown：
https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/sculpting.md
瀏覽器轉至繁中頁（頁面註明 AI 翻譯），語義依英文原文，不依翻譯推論。實讀全部步驟；實看三段約 30 秒影片，每 3 秒取樣接觸表；另看精確位置全尺寸：05 的 12 秒，06 的 4／15／26 秒，07 的 9／27 秒。
- https://prod.docsiteassets.roblox.com/assets/art/accessories/creating/Modeling_05.mp4
- https://prod.docsiteassets.roblox.com/assets/art/accessories/creating/Modeling_06.mp4
- https://prod.docsiteassets.roblox.com/assets/art/accessories/creating/Modeling_07.mp4

可見流程：先用 Elastic Deform 拉衣殼包住人體；Cloth 後胸腹、背部與手臂有人體穿出斑塊；下一段用 Elastic Deform 修正包覆。06 的 4 秒還是較平滑衣面，15 秒背部出現穿出區，26 秒前面與上臂也可見。07 的 9／27 秒主要穿出區已收回。這是 A pose 長袖，非 T pose 寬短袖；UI 沒有展示碰撞設定，不能推論人體已啟用碰撞或所有筆刷都受其保護。

## 判斷：可學，但不直接套
可重用方法：把「衣殼先包住支撐形體」、「局部加皺」、「再檢查四周包覆」當三個不同步驟；不要把出現皺褶視為完成，也不要把可見人體誤認成生效的碰撞體。
仍不足：上述示範沒有給出本角色水平短袖的肩頂支撐、腋下垂落、袖口回折與主折線之間的建構順序。直接把 Grab、Dynamic 或 Elastic Deform 用於失敗彎管，仍會是自己的猜測。
本輪選擇停止建模，不做名義 A/B，不把作者截圖當自己的渲染，不修改 iteration04、sleeve-lower-contour 或任何舊練習。

## 下一個必要資料／有界驗證
需要能看清「肩頂到腋下、再到短袖口」的形體建構示範，最好有水平手臂和未加皺衣殼。若只取得 A pose 長袖，必須先明示姿勢與鬆量轉換假設，不能直接聲稱學會目標短袖。
有了該證據後，首個小練習應只驗證正確衣殼的大形與空間，不立即加密褶皺；正側背斜角與原圖輪廓逐項比較，支撐物只能是工作參照，不當完成服裝。

## 公開版範圍與復現限制

這是歷史實驗筆記；本文提到的模型、腳本、渲染、量測檔與原始參考圖均未包含於本倉庫，檔名只用於說明實驗，不是下載連結。此文字版不能單獨重跑該實驗，也不構成對結果的獨立重驗。來源讀看範圍保留原紀錄，未在公開整理時重新觀看。

[方法索引](../../LEARNING_INDEX.md) · [復現說明](../../REPRODUCING.md)
