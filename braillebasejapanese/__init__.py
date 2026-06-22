from braillebase import *

class BrailleBaseJapanese(BrailleBase):
    def __init__(self):

        """
        Registed Letter:
        あ, い, う, え, お, か, き, く, け, こ, さ, し, す, せ, そ, た, ち, つ, て, と, な, に, ぬ, ね, の, は, ひ, ふ, へ, ほ, ま, み, む, め, も, や, ゆ, よ, ら, り, る, れ, ろ, わ, ゐ, ゑ, を, ん

        が, ぎ, ぐ, げ, ご, ざ, じ, ず, ぜ, ぞ, だ, ぢ, づ, で, ど, ば, び, ぶ, べ, ぼ, ぱ, ぴ, ぷ, ぺ, ぽ

        きゃ, きゅ, きょ, ぎゃ, ぎゅ, ぎょ, しゃ, しゅ, しょ, じゃ, じゅ, じょ, ちゃ, ちゅ, ちょ, ぢゃ, ぢゅ, ぢょ, にゃ, にゅ, にょ, ひゃ, ひゅ, ひょ, びゃ, びゅ, びょ, ぴゃ, ぴゅ, ぴょ, みゃ, みゅ, みょ, りゃ, りゅ, りょ

        っ, ー

        ア, イ, ウ, エ, オ, カ, キ, ク, ケ, コ, サ, シ, ス, セ, ソ, タ, チ, ツ, テ, ト, ナ, ニ, ヌ, ネ, ノ, ハ, ヒ, フ, ヘ, ホ, マ, ミ, ム, メ, モ, ヤ, ユ, ヨ, ラ, リ, ル, レ, ロ, ワ, ヰ, ヱ, ヲ, ン

        ガ, ギ, グ, ゲ, ゴ, ザ, ジ, ズ, ゼ, ゾ, ダ, ヂ, ヅ, デ, ド, バ, ビ, ブ, ベ, ボ, パ, ピ, プ, ペ, ポ

        キャ, キュ, キョ, ギャ, ギュ, ギョ, シャ, シュ, ショ, ジャ, ジュ, ジョ, チャ, チュ, チョ, ヂャ, ヂュ, ヂョ, ニャ, ニュ, ニョ, ヒャ, ヒュ, ヒョ, ビャ, ビュ, ビョ, ピャ, ピュ, ピョ, ミャ, ミュ, ミョ, リャ, リュ, リョ

        イェ, ウィ, ウェ, ウォ, キェ, クァ, クィ, クェ, クォ, グァ, グィ, グェ, グォ, シェ, ジェ, スィ, ズィ, チェ, ツァ, ツィ, ツェ, ツォ, ティ, ディ, テュ, デュ, トゥ, ドゥ, ニェ, ヒェ, ファ, フィ, フェ, フォ, フュ, フョ, ヴァ, ヴィ, ヴェ, ヴォ, ヴュ, ヴョ, ヴ

        ッ

        。, 、, ？, ！, ・, ?, !, ―, …, 「, 」, 『, 』, ～, (, ), ((, )), →, ←, ○, △, □, ×, ％, ＆, ＠, ＃, ＊, @, -, ., /, :, _, ~
        """
        super().__init__()
        #ひ
        self.setting_braille_rules_uppercase("⠠", "⠠") #2026/06/08

        self.append_special_braille_letter_rules_CJK("あ", ["⠁"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("い", ["⠃"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("う", ["⠉"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("え", ["⠋"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("お", ["⠊"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("か", ["⠡"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("き", ["⠣"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("く", ["⠩"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("け", ["⠫"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("こ", ["⠪"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("さ", ["⠱"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("し", ["⠳"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("す", ["⠹"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("せ", ["⠻"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("そ", ["⠺"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("た", ["⠕"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ち", ["⠗"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("つ", ["⠝"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("て", ["⠟"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("と", ["⠞"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("な", ["⠅"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("に", ["⠇"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぬ", ["⠍"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ね", ["⠏"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("の", ["⠎"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("は", ["⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ひ", ["⠧"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ふ", ["⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("へ", ["⠯"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ほ", ["⠮"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ま", ["⠵"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("み", ["⠷"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("む", ["⠽"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("め", ["⠿"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("も", ["⠾"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("や", ["⠌"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ゆ", ["⠬"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("よ", ["⠜"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ら", ["⠑"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("り", ["⠓"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("る", ["⠙"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("れ", ["⠛"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ろ", ["⠚"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("わ", ["⠄"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ゐ", ["⠰"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ゑ", ["⠲"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("を", ["⠔"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ん", ["⠴"]) #2026/05/18 #2026/05/18
        # 濁音
        self.append_special_braille_letter_rules_CJK("が", ["⠐", "⠡"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぎ", ["⠐", "⠣"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぐ", ["⠐", "⠩"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("げ", ["⠐", "⠫"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ご", ["⠐", "⠪"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ざ", ["⠐", "⠱"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("じ", ["⠐", "⠳"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ず", ["⠐", "⠹"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぜ", ["⠐", "⠻"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぞ", ["⠐", "⠺"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("だ", ["⠐", "⠕"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぢ", ["⠐", "⠗"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("づ", ["⠐", "⠝"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("で", ["⠐", "⠟"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ど", ["⠐", "⠞"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ば", ["⠐", "⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("び", ["⠐", "⠧"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぶ", ["⠐", "⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("べ", ["⠐", "⠯"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぼ", ["⠐", "⠮"]) #2026/05/18 #2026/05/18
        # 半濁音
        self.append_special_braille_letter_rules_CJK("ぱ", ["⠠", "⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぴ", ["⠠", "⠧"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぷ", ["⠠", "⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぺ", ["⠠", "⠯"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぽ", ["⠠", "⠮"]) #2026/05/18 #2026/05/18
        #拗音
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_special_braille_letter_rules_CJK("きゃ", ["⠈", "⠡"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("きゅ", ["⠈", "⠩"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("きょ", ["⠈", "⠪"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ぎゃ", ["⠘", "⠡"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぎゅ", ["⠘", "⠩"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぎょ", ["⠘", "⠪"]) #2026/05/18 #2026/05/18

        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_special_braille_letter_rules_CJK("しゃ", ["⠈", "⠱"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("しゅ", ["⠈", "⠹"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("しょ", ["⠈", "⠺"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("じゃ", ["⠘", "⠱"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("じゅ", ["⠘", "⠹"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("じょ", ["⠘", "⠺"]) #2026/05/18 #2026/05/18

        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_special_braille_letter_rules_CJK("ちゃ", ["⠈", "⠕"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ちゅ", ["⠈", "⠝"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ちょ", ["⠈", "⠞"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ぢゃ", ["⠘", "⠕"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぢゅ", ["⠘", "⠝"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぢょ", ["⠘", "⠞"]) #2026/05/18 #2026/05/18

        # にゃ にゅ にょ
        self.append_special_braille_letter_rules_CJK("にゃ", ["⠈", "⠅"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("にゅ", ["⠈", "⠍"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("にょ", ["⠈", "⠎"]) #2026/05/18 #2026/05/18

        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_special_braille_letter_rules_CJK("ひゃ", ["⠈", "⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ひゅ", ["⠈", "⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ひょ", ["⠈", "⠮"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("びゃ", ["⠘", "⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("びゅ", ["⠘", "⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("びょ", ["⠘", "⠮"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ぴゃ", ["⠨", "⠥"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぴゅ", ["⠨", "⠭"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("ぴょ", ["⠨", "⠮"]) #2026/05/18 #2026/05/18

        # みゃ みゅ みょ
        self.append_special_braille_letter_rules_CJK("みゃ", ["⠈", "⠵"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("みゅ", ["⠈", "⠽"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("みょ", ["⠈", "⠾"]) #2026/05/18 #2026/05/18

        # りゃ りゅ りょ
        self.append_special_braille_letter_rules_CJK("りゃ", ["⠈", "⠑"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("りゅ", ["⠈", "⠙"]) #2026/05/18 #2026/05/18
        self.append_special_braille_letter_rules_CJK("りょ", ["⠈", "⠚"]) #2026/05/18 #2026/05/18

        self.append_special_braille_letter_rules_CJK("ぁ", ["⠡"])
        self.append_special_braille_letter_rules_CJK("ぃ", ["⠣"])
        self.append_special_braille_letter_rules_CJK("ぅ", ["⠩"])
        self.append_special_braille_letter_rules_CJK("ぇ", ["⠫"])
        self.append_special_braille_letter_rules_CJK("ぉ", ["⠹"])

        self.append_special_braille_letter_rules_CJK("ゃ", ["⠈"])
        self.append_special_braille_letter_rules_CJK("ゅ", ["⠊"])
        self.append_special_braille_letter_rules_CJK("ょ", ["⠌"])
        #促音
        self.append_special_braille_letter_rules_CJK("っ", ["⠂"]) #2026/05/18 2026/06/08
        #長音 
        self.append_special_braille_letter_rules_CJK("ー", ["⠒"]) #2026/05/18

        # カタカナ
        self.append_special_braille_letter_rules_CJK("ア", ["⠁"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("イ", ["⠃"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ウ", ["⠉"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("エ", ["⠋"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("オ", ["⠊"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("カ", ["⠡"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("キ", ["⠣"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ク", ["⠩"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ケ", ["⠫"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("コ", ["⠪"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("サ", ["⠱"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("シ", ["⠳"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ス", ["⠹"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("セ", ["⠻"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ソ", ["⠺"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("タ", ["⠕"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("チ", ["⠗"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ツ", ["⠝"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("テ", ["⠟"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ト", ["⠞"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ナ", ["⠅"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ニ", ["⠇"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヌ", ["⠍"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ネ", ["⠏"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ノ", ["⠎"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ハ", ["⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヒ", ["⠧"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("フ", ["⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヘ", ["⠯"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ホ", ["⠮"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("マ", ["⠵"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ミ", ["⠷"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ム", ["⠽"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("メ", ["⠿"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("モ", ["⠾"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヤ", ["⠌"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ユ", ["⠬"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヨ", ["⠜"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ラ", ["⠑"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("リ", ["⠓"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ル", ["⠙"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("レ", ["⠛"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ロ", ["⠚"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ワ", ["⠄"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヰ", ["⠰"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヱ", ["⠲"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヲ", ["⠔"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ン", ["⠴"]) #2026/05/30
        # カタカナ 濁音
        self.append_special_braille_letter_rules_CJK("ガ", ["⠐", "⠡"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ギ", ["⠐", "⠣"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("グ", ["⠐", "⠩"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ゲ", ["⠐", "⠫"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ゴ", ["⠐", "⠪"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ザ", ["⠐", "⠱"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ジ", ["⠐", "⠳"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ズ", ["⠐", "⠹"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ゼ", ["⠐", "⠻"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ゾ", ["⠐", "⠺"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ダ", ["⠐", "⠕"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヂ", ["⠐", "⠗"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヅ", ["⠐", "⠝"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("デ", ["⠐", "⠟"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ド", ["⠐", "⠞"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("バ", ["⠐", "⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ビ", ["⠐", "⠧"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ブ", ["⠐", "⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ベ", ["⠐", "⠯"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ボ", ["⠐", "⠮"]) #2026/05/30
        # カタカナ 半濁音
        self.append_special_braille_letter_rules_CJK("パ", ["⠠", "⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ピ", ["⠠", "⠧"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("プ", ["⠠", "⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ペ", ["⠠", "⠯"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ポ", ["⠠", "⠮"]) #2026/05/30
        # カタカナ 拗音 (youon)
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_special_braille_letter_rules_CJK("キャ", ["⠈", "⠡"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("キュ", ["⠈", "⠩"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("キョ", ["⠈", "⠪"]) #2026/05/30

        self.append_special_braille_letter_rules_CJK("ギャ", ["⠘", "⠡"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ギュ", ["⠘", "⠩"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ギョ", ["⠘", "⠪"]) #2026/05/30
        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_special_braille_letter_rules_CJK("シャ", ["⠈", "⠱"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("シュ", ["⠈", "⠹"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ショ", ["⠈", "⠺"]) #2026/05/30

        self.append_special_braille_letter_rules_CJK("ジャ", ["⠘", "⠱"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ジュ", ["⠘", "⠹"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ジョ", ["⠘", "⠺"]) #2026/05/30
        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_special_braille_letter_rules_CJK("チャ", ["⠈", "⠕"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("チュ", ["⠈", "⠝"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("チョ", ["⠈", "⠞"]) #2026/05/30

        self.append_special_braille_letter_rules_CJK("ヂャ", ["⠘", "⠕"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヂュ", ["⠘", "⠝"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヂョ", ["⠘", "⠞"]) #2026/05/30
        # にゃ にゅ にょ
        self.append_special_braille_letter_rules_CJK("ニャ", ["⠈", "⠅"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ニュ", ["⠈", "⠍"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ニョ", ["⠈", "⠎"]) #2026/05/30
        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_special_braille_letter_rules_CJK("ヒャ", ["⠈", "⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヒュ", ["⠈", "⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ヒョ", ["⠈", "⠮"]) #2026/05/30

        self.append_special_braille_letter_rules_CJK("ビャ", ["⠘", "⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ビュ", ["⠘", "⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ビョ", ["⠘", "⠮"]) #2026/05/30

        self.append_special_braille_letter_rules_CJK("ピャ", ["⠨", "⠥"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ピュ", ["⠨", "⠭"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ピョ", ["⠨", "⠮"]) #2026/05/30
        # みゃ みゅ みょ
        self.append_special_braille_letter_rules_CJK("ミャ", ["⠈", "⠵"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ミュ", ["⠈", "⠽"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("ミョ", ["⠈", "⠾"]) #2026/05/30
        # りゃ りゅ りょ
        self.append_special_braille_letter_rules_CJK("リャ", ["⠈", "⠑"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("リュ", ["⠈", "⠙"]) #2026/05/30
        self.append_special_braille_letter_rules_CJK("リョ", ["⠈", "⠚"]) #2026/05/30

        #イ段 / ウ段 Special
        self.append_special_braille_letter_rules_CJK("イェ", ["⠈", "⠋"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ウィ", ["⠢", "⠃"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ウェ", ["⠢", "⠋"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ウォ", ["⠢", "⠊"]) #2026/05/30 2026/06/08
        #キ系
        self.append_special_braille_letter_rules_CJK("キェ", ["⠈", "⠫"]) #2026/05/30 2026/06/08
        #ク系 / グ系
        self.append_special_braille_letter_rules_CJK("クァ", ["⠢", "⠡"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("クィ", ["⠢", "⠣"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("クェ", ["⠢", "⠫"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("クォ", ["⠢", "⠪"]) #2026/05/30 2026/06/08
        
        self.append_special_braille_letter_rules_CJK("グァ", ["⠲", "⠡"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("グィ", ["⠲", "⠣"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("グェ", ["⠲", "⠫"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("グォ", ["⠲", "⠪"]) #2026/05/30 2026/06/08
        #シ系 / ス系 / ズ系
        self.append_special_braille_letter_rules_CJK("シェ", ["⠈", "⠻"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ジェ", ["⠘", "⠻"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("スィ", ["⠈", "⠳"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ズィ", ["⠘", "⠳"]) #2026/05/30 2026/06/08
        #チ系
        self.append_special_braille_letter_rules_CJK("チェ", ["⠈", "⠟"]) #2026/05/30 2026/06/08
        #ツ系
        self.append_special_braille_letter_rules_CJK("ツァ", ["⠢", "⠕"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ツィ", ["⠢", "⠗"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ツェ", ["⠢", "⠟"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ツォ", ["⠢", "⠞"]) #2026/05/30 2026/06/08

        #ティ系 / ディ系 / トゥ系 / ドゥ系
        self.append_special_braille_letter_rules_CJK("ティ", ["⠈", "⠗"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ディ", ["⠘", "⠗"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("テュ", ["⠨", "⠝"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("デュ", ["⠸", "⠝"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("トゥ", ["⠢", "⠝"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ドゥ", ["⠲", "⠝"]) #2026/05/30 2026/06/08

        #ニェ系 / ヒェ系
        self.append_special_braille_letter_rules_CJK("ニェ", ["⠈", "⠏"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヒェ", ["⠈", "⠯"]) #2026/05/30 2026/06/08

        #F系
        self.append_special_braille_letter_rules_CJK("ファ", ["⠢", "⠥"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("フィ", ["⠢", "⠧"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("フェ", ["⠢", "⠯"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("フォ", ["⠢", "⠮"]) #2026/05/30 2026/06/08

        self.append_special_braille_letter_rules_CJK("フュ", ["⠨", "⠬"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("フョ", ["⠨", "⠜"]) #2026/05/30 2026/06/08

        #V系
        self.append_special_braille_letter_rules_CJK("ヴァ", ["⠲", "⠥"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヴィ", ["⠲", "⠧"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヴェ", ["⠲", "⠯"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヴォ", ["⠲", "⠮"]) #2026/05/30 2026/06/08

        self.append_special_braille_letter_rules_CJK("ヴュ", ["⠸", "⠭"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヴョ", ["⠸", "⠮"]) #2026/05/30 2026/06/08
        self.append_special_braille_letter_rules_CJK("ヴ",  ["⠐", "⠉"]) #2026/05/30 2026/06/08

        # Katakana small vowels
        self.append_special_braille_letter_rules_CJK("ァ", ["⠡"])
        self.append_special_braille_letter_rules_CJK("ィ", ["⠣"])
        self.append_special_braille_letter_rules_CJK("ゥ", ["⠩"])
        self.append_special_braille_letter_rules_CJK("ェ", ["⠫"])
        self.append_special_braille_letter_rules_CJK("ォ", ["⠹"])

        # Katakana small ya/yu/yo
        self.append_special_braille_letter_rules_CJK("ャ", ["⠈"])
        self.append_special_braille_letter_rules_CJK("ュ", ["⠊"])
        self.append_special_braille_letter_rules_CJK("ョ", ["⠌"])

        # カタカナ #促音
        self.append_special_braille_letter_rules_CJK("ッ", ["⠂"]) #2026/06/08

        # romanji
        self.append_special_braille_letter_rules_CJK("外字", ["⠰"]) #2026/06/08 #Temporary
        self.append_braille_letter("a", ["⠁"]) #2026/06/08
        self.append_braille_letter("b", ["⠃"]) #2026/06/08
        self.append_braille_letter("c", ["⠉"]) #2026/06/08
        self.append_braille_letter("d", ["⠙"]) #2026/06/08
        self.append_braille_letter("e", ["⠑"]) #2026/06/08
        self.append_braille_letter("f", ["⠋"]) #2026/06/08
        self.append_braille_letter("g", ["⠛"]) #2026/06/08
        self.append_braille_letter("h", ["⠓"]) #2026/06/08
        self.append_braille_letter("i", ["⠊"]) #2026/06/08
        self.append_braille_letter("j", ["⠚"]) #2026/06/08
        self.append_braille_letter("k", ["⠅"]) #2026/06/08
        self.append_braille_letter("l", ["⠇"]) #2026/06/08
        self.append_braille_letter("m", ["⠍"]) #2026/06/08
        self.append_braille_letter("n", ["⠝"]) #2026/06/08
        self.append_braille_letter("o", ["⠕"]) #2026/06/08
        self.append_braille_letter("p", ["⠏"]) #2026/06/08
        self.append_braille_letter("q", ["⠟"]) #2026/06/08
        self.append_braille_letter("r", ["⠗"]) #2026/06/08
        self.append_braille_letter("s", ["⠎"]) #2026/06/08
        self.append_braille_letter("t", ["⠞"]) #2026/06/08
        self.append_braille_letter("u", ["⠥"]) #2026/06/08
        self.append_braille_letter("v", ["⠧"]) #2026/06/08
        self.append_braille_letter("w", ["⠺"]) #2026/06/08
        self.append_braille_letter("x", ["⠭"]) #2026/06/08
        self.append_braille_letter("y", ["⠽"]) #2026/06/08
        self.append_braille_letter("z", ["⠵"]) #2026/06/08
        
        self.append_special_braille_letter_rules_uppercase("A", ["⠁"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("B", ["⠃"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("C", ["⠉"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("D", ["⠙"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("E", ["⠑"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("F", ["⠋"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("G", ["⠛"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("H", ["⠓"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("I", ["⠊"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("J", ["⠚"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("K", ["⠅"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("L", ["⠇"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("M", ["⠍"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("N", ["⠝"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("O", ["⠕"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("P", ["⠏"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("Q", ["⠟"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("R", ["⠗"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("S", ["⠎"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("T", ["⠞"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("U", ["⠥"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("V", ["⠧"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("W", ["⠺"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("X", ["⠭"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("Y", ["⠽"]) #2026/06/08
        self.append_special_braille_letter_rules_uppercase("Z", ["⠵"]) #2026/06/08


        #number
        self.append_braille_letter("⠼", ["⠼"]) #2026/05/31
        self.append_braille_letter("1", ["⠁"]) #2026/05/31
        self.append_braille_letter("2", ["⠃"]) #2026/05/31
        self.append_braille_letter("3", ["⠉"]) #2026/05/31
        self.append_braille_letter("4", ["⠙"]) #2026/05/31
        self.append_braille_letter("5", ["⠑"]) #2026/05/31
        self.append_braille_letter("6", ["⠋"]) #2026/05/31
        self.append_braille_letter("7", ["⠛"]) #2026/05/31
        self.append_braille_letter("8", ["⠓"]) #2026/05/31
        self.append_braille_letter("9", ["⠊"]) #2026/05/31
        self.append_braille_letter("0", ["⠚"]) #2026/05/31


        # Simb 符  号
        self.append_special_braille_letter_rules_CJK("。", ["⠲", "⠀"]) #2026/05/18 #2026/06/14
        self.append_special_braille_letter_rules_CJK("、", ["⠰", "⠀"]) #2026/05/18 #2026/06/14
        self.append_special_braille_letter_rules_CJK("？", ["⠢", "⠀"]) #2026/05/18 #2026/06/14
        self.append_special_braille_letter_rules_CJK("！", ["⠖", "⠀"]) #2026/05/18 #2026/06/14
        self.append_special_braille_letter_rules_CJK("・", ["⠐", "⠀"]) #2026/05/18 #2026/06/14
        self.append_special_braille_letter_rules_CJK(":", ["⠐", "⠂", "⠀"]) #2026/05/31  #2026/06/08 #2026/06/14
        #International
        self.append_special_braille_letter_rules_CJK("?", ["⠢", "⠀"]) #2026/05/18
        self.append_special_braille_letter_rules_CJK("!", ["⠖", "⠀"]) #2026/05/18

        #棒線 / 点線
        self.append_special_braille_letter_rules_CJK("―", ["⠒","⠒"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("…", ["⠂","⠂","⠂"]) #2026/05/31

        #第１カギ / ふたえカギ / 波線 / 第１カッコ / 二重カッコ
        self.append_special_braille_letter_rules_CJK("「", ["⠰", "⠄"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("」", ["⠠", "⠆"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("『", ["⠰", "⠤"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("』", ["⠤", "⠆"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("～", ["⠤", "⠤"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("(", ["⠐", "⠶"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK(")", ["⠶", "⠂"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("((", ["⠰", "⠶"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("))", ["⠶", "⠆"]) #2026/05/31
        #right / left
        self.append_special_braille_letter_rules_CJK("→", ["⠒", "⠒", "⠕"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("←", ["⠪", "⠒", "⠒"]) #2026/05/31
        #○ / △ / □ / ×
        self.append_special_braille_letter_rules_CJK("○", ["⠐", "⠵"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("△", ["⠐", "⠷"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("□", ["⠐", "⠽"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("×", ["⠐", "⠿"]) #2026/05/31

        self.append_special_braille_letter_rules_CJK("％", ["⠰", "⠏"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("   ", ["⠰", "⠯"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("＠", ["⠰", "⠪"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("＃", ["⠰", "⠩"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("＊", ["⠰", "⠡"]) #2026/05/31

        self.append_special_braille_letter_rules_CJK("@", ["⠪"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("-", ["⠤"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK(".", ["⠲"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK(",", ["⠂"]) #2026/06/08
        self.append_special_braille_letter_rules_CJK("/", ["⠌"]) #2026/05/31 
        self.append_special_braille_letter_rules_CJK(";", ["⠆"]) #2026/06/08
        self.append_special_braille_letter_rules_CJK("'", ["⠄"]) #2026/06/08

        self.append_special_braille_letter_rules_CJK("_", ["⠐", "⠤"]) #2026/05/31
        self.append_special_braille_letter_rules_CJK("~", ["⠐", "⠉"]) #2026/05/31

        self.append_special_braille_letter_rules_CJK("%", ["⠰", "⠏"])
        self.append_special_braille_letter_rules_CJK("&", ["⠈", "⠯"]) #2026/06/08
        self.append_special_braille_letter_rules_CJK("#", ["⠰", "⠩"])
        self.append_special_braille_letter_rules_CJK("*", ["⠰", "⠡"])
