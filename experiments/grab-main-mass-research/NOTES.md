# 2026-10-29 20:06 UTC — Grab 與主髮量研究（無新模型）

## 有用結論
- 前輪把擷取薄片用自製權重拉成長葉，沒有解決主髮量。此輪不再用任意頂點拉伸代替作者筆刷操作。
- Blender Grab 是移動起筆範圍頂點的工具，不是自動保持髮塊體積的保證。官方說明的「Grab Silhouette」也不是保體積：它依視角與起筆位置，只抓網格曲率的一側。
- 官方4.3手冊已完整讀到；Blender Studio課程內容未讀。

## 確實讀了什麼
### Blender 4.3 Grab 官方手冊
https://docs.blender.org/manual/en/4.3/sculpt_paint/sculpting/brushes/grab.html

透過瀏覽器讀到 Grab、Brush Settings、Grab Active Vertex、Grab Silhouette、2D Grab 全段。
- Grab 移動起筆瞬間筆刷半徑內的頂點，跟隨畫面中的游標。
- Radius/Strength 不支援筆壓；Normal Radius僅影響顯示；Auto-Smooth不支援。
- Active Vertex 對高亮頂點施最大強度，適合低模/修改器網格辨識。
- Silhouette 依視角與起筆決定只拉曲率的一側。
- Projected falloff可向視窗深度無限影響，寬幅移形時可能連背面一起抓。

以上是讀到工具行為，不是看過雕髮動作，也不是已掌握維持主量的方法。

### Pablo Muñoz Gómez 作者文字教學
https://www.pablander.academy/tutorials/sculpting-stylised-hair-in-zbrush

確實讀完整步驟摘要：低解析建立主要髮量、辨識大髮塊、依分區建立方向、逐步加次級量與細節，最後可大筆刷Move修輪廓。作者使用ZBrush及部分自製筆刷，文字也列替代筆刷。此輪沒有下載筆刷或執行陌生工具。

## 未能看見的操作
作者嵌入影片導向：
https://www.youtube.com/watch?v=WFqyj6lKgik
標題 Stylised Sculpted Hair in ZBrush，作者 Pablo Muñoz Gómez，播放器長43:16。

已嘗試頁面播放、原YouTube、跳到21:41、降360p。0:00與21:41畫面均黑屏緩衝；字幕能載入並不代表筆刷畫面可見。沒有看見實際起筆/拖動/放開序列，無法記錄作者的精確筆刷動作、半徑、支承位置或推拉幅度。不猜測串流失敗的技術原因。

Blender Studio：
https://studio.blender.org/training/speed-sculpting/5cb8879fd6963c01ab9b0fe2/
瀏覽器顯示 Login to view this content / Join。沒有登入、購買或繞過；沒有看過課程內容。

## 本輪結果與下一缺口
- 無新模型、無新模型渲染、無原圖改善對照。前輪模型與iteration04均未改動。
- 下一步需要能實際播放的原作者短示範：能看清大筆刷如何對已有主髮量作短距推拉、影響範圍如何避開根部/背面，以及轉視角檢查的時機。
- 待這段操作可觀察後，再用原生Blender筆刷小範圍測試。ZBrush Move與Blender Grab只可類比功能目的，不能直接視為相同半徑/衰減/保量算法。
- 原圖被遮擋的支承區與頭部深度仍未知；本輪沒有新增假設去補造根部。

## 公開版範圍與復現限制

本文是既有實驗筆記的整理；「實讀／實看」與數值結果指當時紀錄，本次公開整理未獨立重跑。原始 `.blend`、實驗腳本、渲染圖、研究用三視圖及第三方教材圖片均未隨本文提供。文中檔名只用於說明歷史證據，不是可下載附件；不可僅憑此文字版宣稱已復現或驗收角色。


## 公開附圖

此篇沒有附上可公開的自製實驗圖；不以第三方教材影格或私人操作畫面代替成果。

[固定角色原始三視圖](../../images/reference/character-three-views.png)
