# H1 撤回：先修正實驗輸入契約，不把已知雙尖重當新發現

2026-10-30 18:36（Asia/Taipei）。**本輪為實驗前提核對及撤回，不是新髮型、接根成功或新學會雙尖問題。沒有可交付的新模型／比較圖。**

## 問題與實際讀回
已讀 LEARNING_INDEX、oblique-reference-limits/VALIDATION_SPEC及NOTES、forelock-registration-audit、forelock-root-flow、supported-hair-root。進一步逐行追查 forelock-registration-audit/build.py、whole-profile-retest/build.py、front-hair-layer/build.py 和 forelock-root-flow/build.py。

上一輪規格要求從註冊診斷 B 出發，找「實際後邊界」沿既有根切線首次命中04局部髮底代理。核對後發現：**這個指定輸入根本不是已有有限根邊界的試驗件。** 因而應撤回H1，而不是把未開始的接觸試驗寫成接觸失敗。

## 輸入血緣證據
1. 註冊診斷的 source-input/local-hair.blend、whole-profile-retest/B-aligned-arch.blend、forelock-root-flow/source-input/context.blend 三者SHA256相同：`e61febdb7ccd487c5dda9bca837d2b9c704f366af0679e804cf218833eb9ab49`。
2. whole-profile-retest 的 B 只將主高束的導向截面改成共線拱形，另載入舊 `C front arc` 作固定上下文。**B-aligned-arch 的 B 不是 B-finite-root-strip 的 B。**
3. registration-audit 再共同等比映射上述舊三束，沒有載入 forelock-root-flow 的 B/C 根片。前弧物件是 `Fixed historical context C front arc`。
4. 對該指定物件的只讀核對：275頂點、553邊、280面；所有邊皆由兩面共用，開放邊界0；頂點273及274各由7三角面匯入。這只確認**08:36已知的雙尖閉合結構仍在本輪輸入**，不是重新發現或能力進步。
5. forelock-root-flow B 才另外建立可編輯的41×7根片控制面，並加Subdivision/Solidify；C在此基礎彎曲。但B/C已分別有懸片及側耳／穿束失敗，不能因有邊界就暗換成本輪基線。

## 判定與停止
H1 = **不適用／撤回指定輸入上的接根實驗**。沒有符合規格的後邊界，故未射線測試、未建立延伸，也沒有「首次命中cap／皮膚」的結果。封閉尖端附近可以估一條方向，但它不能替代已定義的根表面邊界；否則已變成另一次刪面／重建根的不同假設。

停止Y／角度掃描、任意新片、改鏡頭與改cap；Y0仍只是可撤回座標假設，cap仍是未驗證代理，04不改。沒有證據能推論「cap接不到」或「沿切線一定不能接上」。

## 來源實讀範圍與方法適用性
本輪讀回前輪來源紀錄，**沒有新讀外部教程或新看操作影片**：
- [Jasper Ritsema](https://80.lv/articles/stylized-character-from-2d-to-3d)：前輪讀Matching the reference／Face／Hair，實看短尖髮概念、Sphere／Refining blockout階段及前後斜線框。僅支持主視相似與其他視角可用性分工，不提供本案邊界／根深。
- [Mido Lai](https://80.lv/articles/character-production-workflow-overview)：前輪讀Blockout／Hair、看兩階段多視圖；支持固定比較視角與大形先行，非根部數值。
- [UCBUGG](https://www.ucbugg.com/labs/modeling/polygon-hair-modeling)：08:36讀Front Hair／Side Hair／Notes，實看前額面、分線向上延伸及後緣接續三圖；可借鑑根後緣延續，但長瀏海造型不同。當前閉合雙尖並不具備那種後緣。

造型相似與三維可用性本輪皆**未開始新的候選驗證**；不得用拓撲數字代替美術進步，也不將作者案例當作本輪射線／接根成功證據。

## 本輪真正留下的戒條與下一步
先核對「模型分支、實際物件、可操作邊界」三者，再寫變形假設；同名A/B/C只是各實驗局部標籤，不能跨資料夾視為同一幾何版本。已知不具前提的輸入應在開工前攔下，不能靠新渲染把已知問題包裝成進步。

下一個缺口仍是：如何有據建立與可見外緣相容的**有方向根截面／表面後緣**。下一規格須先明列輸入SHA、物件名、控制面邊界和已知失敗；若選舊B/C修正，須先有針對懸片／外翻的全新方法依據，不能直接重新調位移。H1射線接根不得原樣再排。

## 保存及誠實限制
本公開版只附撤回記錄，沒有新模型或新圖。指定輸入、只讀診斷腳本與來源腳本另私存，不能由此公開庫獨立重建。初次不當啟動的重複舊幾何渲染已中止，不完整前／側兩張不交付，不列為研究成果或恢復包內容。沒有射線結果，也沒有四向新候選驗證。原04不變；GitHub仍待原核准，未寫入／重試。

[前輪規格及撤回註記](../oblique-reference-limits/VALIDATION_SPEC.md) · [來源註冊診斷](../forelock-registration-audit/NOTES.md) · [恢復限制](../../REPRODUCING.md)
