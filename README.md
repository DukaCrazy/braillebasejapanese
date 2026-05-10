-        `Weighted average accuracy: ≈ 96–97%`

🇺🇸 EN
Braille table for the Japanese language.
This library is built on top of BrailleBase.
The current version accepts keys (characters) composed of only one Japanese character, while the values (braille cells) may contain as many cells as needed.
Note:
Combinations that form yōon — such as きゃ, きゅ, きょ, ひゃ, ひゅ, ひょ, ぴゃ, ぴゅ, ぴょ — are written in Japanese using two characters (for example: ひ + ゃ = ひゃ).
Since the current version only accepts single‑character keys, these combinations are interpreted separately.
For example, when processing ひゃ, the library outputs:
- ひ
- ゃ (small や)
instead of recognizing ひゃ as a single combined syllable.

🇯🇵 JP
日本語点字のテーブルです。
このライブラリは BrailleBase を基盤として動作しています。
現行バージョンでは、キー（文字）は 1 文字のみ登録でき、
値（点字）は必要なだけ複数セルを登録できます。
注意：
拗音（きゃ・きゅ・きょ、ひゃ・ひゅ・ひょ、ぴゃ・ぴゅ・ぴょ など）は、
本来 2 文字の組み合わせ（例：ひ + ゃ = ひゃ）で 1 音を表します。
しかし現行バージョンではキーが 1 文字しか登録できないため、
「ひゃ」は次のように別々に処理されます：
- ひ
- ゃ（小さいや）
つまり、ひゃ として 1 つの音にまとめることができません。

🇮🇹 IT
Tabella Braille per la lingua giapponese.
Questa libreria utilizza BrailleBase come struttura principale.
L’attuale versione accetta chiavi composte da un solo carattere giapponese, mentre i valori (celle braille) possono contenere tutte le celle necessarie.
Nota:
Le combinazioni che formano gli yōon — come きゃ, きゅ, きょ, ひゃ, ひゅ, ひょ, ぴゃ, ぴゅ, ぴょ — sono scritte in giapponese usando due caratteri (ad esempio: ひ + ゃ = ひゃ).
Poiché l’attuale versione accetta solo chiavi di un singolo carattere, queste combinazioni vengono interpretate separatamente.
Ad esempio, elaborando ひゃ, la libreria restituisce:
- ひ
- ゃ（や piccola）
invece di riconoscere ひゃ come una sola sillaba composta.

🇧🇷 PT
Tabela de Braille para a língua japonesa.
Esta biblioteca utiliza o BrailleBase como base estrutural.
A versão atual aceita chaves formadas por apenas um caractere japonês, enquanto os valores (brailles) podem conter quantas células forem necessárias.
Observação:
As combinações que formam yōon — como きゃ, きゅ, きょ, ひゃ, ひゅ, ひょ, ぴゃ, ぴゅ, ぴょ — são representadas no japonês por dois caracteres (por exemplo: ひ + ゃ = ひゃ).
Como a versão atual só aceita chaves de um único caractere, essas combinações são interpretadas separadamente.
Por exemplo, ao processar ひゃ, a biblioteca retorna:
- ひ
- ゃ（や pequena）
em vez de reconhecer ひゃ como uma única unidade fonética.
