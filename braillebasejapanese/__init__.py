from braillebase import BrailleBase

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
        self.append_braille_letter("あ", ["⠁"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("い", ["⠃"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("う", ["⠉"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("え", ["⠋"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("お", ["⠊"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("か", ["⠡"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("き", ["⠣"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("く", ["⠩"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("け", ["⠫"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("こ", ["⠪"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("さ", ["⠱"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("し", ["⠳"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("す", ["⠹"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("せ", ["⠻"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("そ", ["⠺"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("た", ["⠕"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ち", ["⠗"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("つ", ["⠝"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("て", ["⠟"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("と", ["⠞"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("な", ["⠅"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("に", ["⠇"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぬ", ["⠍"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ね", ["⠏"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("の", ["⠎"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("は", ["⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひ", ["⠧"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ふ", ["⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("へ", ["⠯"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ほ", ["⠮"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ま", ["⠵"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("み", ["⠷"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("む", ["⠽"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("め", ["⠿"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("も", ["⠾"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("や", ["⠌"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ゆ", ["⠬"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("よ", ["⠜"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ら", ["⠑"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("り", ["⠓"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("る", ["⠙"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("れ", ["⠛"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ろ", ["⠚"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("わ", ["⠄"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ゐ", ["⠰"]) #2026/05/30
        self.append_braille_letter("ゑ", ["⠲"]) #2026/05/30
        self.append_braille_letter("を", ["⠔"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ん", ["⠴"]) #2026/05/18 #2026/05/18
        # 濁音
        self.append_braille_letter("が", ["⠐", "⠡"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎ", ["⠐", "⠣"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぐ", ["⠐", "⠩"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("げ", ["⠐", "⠫"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ご", ["⠐", "⠪"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ざ", ["⠐", "⠱"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("じ", ["⠐", "⠳"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ず", ["⠐", "⠹"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぜ", ["⠐", "⠻"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぞ", ["⠐", "⠺"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("だ", ["⠐", "⠕"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢ", ["⠐", "⠗"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("づ", ["⠐", "⠝"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("で", ["⠐", "⠟"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ど", ["⠐", "⠞"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ば", ["⠐", "⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("び", ["⠐", "⠧"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぶ", ["⠐", "⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("べ", ["⠐", "⠯"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぼ", ["⠐", "⠮"]) #2026/05/18 #2026/05/18
        # 半濁音
        self.append_braille_letter("ぱ", ["⠠", "⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴ", ["⠠", "⠧"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぷ", ["⠠", "⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぺ", ["⠠", "⠯"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぽ", ["⠠", "⠮"]) #2026/05/18 #2026/05/18
        #拗音
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_braille_letter("きゃ", ["⠈", "⠡"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("きゅ", ["⠈", "⠩"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("きょ", ["⠈", "⠪"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぎゃ", ["⠘", "⠡"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎゅ", ["⠘", "⠩"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎょ", ["⠘", "⠪"]) #2026/05/18 #2026/05/18

        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_braille_letter("しゃ", ["⠈", "⠱"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("しゅ", ["⠈", "⠹"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("しょ", ["⠈", "⠺"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("じゃ", ["⠘", "⠱"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("じゅ", ["⠘", "⠹"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("じょ", ["⠘", "⠺"]) #2026/05/18 #2026/05/18

        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_braille_letter("ちゃ", ["⠈", "⠕"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ちゅ", ["⠈", "⠝"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ちょ", ["⠈", "⠞"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぢゃ", ["⠘", "⠕"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢゅ", ["⠘", "⠝"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢょ", ["⠘", "⠞"]) #2026/05/18 #2026/05/18

        # にゃ にゅ にょ
        self.append_braille_letter("にゃ", ["⠈", "⠅"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("にゅ", ["⠈", "⠍"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("にょ", ["⠈", "⠎"]) #2026/05/18 #2026/05/18

        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_braille_letter("ひゃ", ["⠈", "⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひゅ", ["⠈", "⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひょ", ["⠈", "⠮"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("びゃ", ["⠘", "⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("びゅ", ["⠘", "⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("びょ", ["⠘", "⠮"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぴゃ", ["⠨", "⠥"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴゅ", ["⠨", "⠭"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴょ", ["⠨", "⠮"]) #2026/05/18 #2026/05/18

        # みゃ みゅ みょ
        self.append_braille_letter("みゃ", ["⠈", "⠵"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("みゅ", ["⠈", "⠽"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("みょ", ["⠈", "⠾"]) #2026/05/18 #2026/05/18

        # りゃ りゅ りょ
        self.append_braille_letter("りゃ", ["⠈", "⠑"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("りゅ", ["⠈", "⠙"]) #2026/05/18 #2026/05/18
        self.append_braille_letter("りょ", ["⠈", "⠚"]) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぁ", ["⠡"])
        self.append_braille_letter("ぃ", ["⠣"])
        self.append_braille_letter("ぅ", ["⠩"])
        self.append_braille_letter("ぇ", ["⠫"])
        self.append_braille_letter("ぉ", ["⠹"])

        self.append_braille_letter("ゃ", ["⠈"])
        self.append_braille_letter("ゅ", ["⠊"])
        self.append_braille_letter("ょ", ["⠌"])
        #促音
        self.append_braille_letter("っ", ["⠂"]) #2026/05/18
        #長音 
        self.append_braille_letter("ー", ["⠒"]) #2026/05/18

        # カタカナ
        self.append_special_braille_lettr_rules02("ア", ["⠁"]) #2026/05/30
        self.append_special_braille_lettr_rules02("イ", ["⠃"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ウ", ["⠉"]) #2026/05/30
        self.append_special_braille_lettr_rules02("エ", ["⠋"]) #2026/05/30
        self.append_special_braille_lettr_rules02("オ", ["⠊"]) #2026/05/30
        self.append_special_braille_lettr_rules02("カ", ["⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("キ", ["⠣"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ク", ["⠩"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ケ", ["⠫"]) #2026/05/30
        self.append_special_braille_lettr_rules02("コ", ["⠪"]) #2026/05/30
        self.append_special_braille_lettr_rules02("サ", ["⠱"]) #2026/05/30
        self.append_special_braille_lettr_rules02("シ", ["⠳"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ス", ["⠹"]) #2026/05/30
        self.append_special_braille_lettr_rules02("セ", ["⠻"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ソ", ["⠺"]) #2026/05/30
        self.append_special_braille_lettr_rules02("タ", ["⠕"]) #2026/05/30
        self.append_special_braille_lettr_rules02("チ", ["⠗"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ツ", ["⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("テ", ["⠟"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ト", ["⠞"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ナ", ["⠅"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ニ", ["⠇"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヌ", ["⠍"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ネ", ["⠏"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ノ", ["⠎"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ハ", ["⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヒ", ["⠧"]) #2026/05/30
        self.append_special_braille_lettr_rules02("フ", ["⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヘ", ["⠯"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ホ", ["⠮"]) #2026/05/30
        self.append_special_braille_lettr_rules02("マ", ["⠵"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ミ", ["⠷"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ム", ["⠽"]) #2026/05/30
        self.append_special_braille_lettr_rules02("メ", ["⠿"]) #2026/05/30
        self.append_special_braille_lettr_rules02("モ", ["⠾"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヤ", ["⠌"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ユ", ["⠬"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヨ", ["⠜"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ラ", ["⠑"]) #2026/05/30
        self.append_special_braille_lettr_rules02("リ", ["⠓"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ル", ["⠙"]) #2026/05/30
        self.append_special_braille_lettr_rules02("レ", ["⠛"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ロ", ["⠚"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ワ", ["⠄"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヰ", ["⠰"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヱ", ["⠲"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヲ", ["⠔"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ン", ["⠴"]) #2026/05/30
        # カタカナ 濁音
        self.append_special_braille_lettr_rules02("ガ", ["⠐", "⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ギ", ["⠐", "⠣"]) #2026/05/30
        self.append_special_braille_lettr_rules02("グ", ["⠐", "⠩"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ゲ", ["⠐", "⠫"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ゴ", ["⠐", "⠪"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ザ", ["⠐", "⠱"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ジ", ["⠐", "⠳"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ズ", ["⠐", "⠹"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ゼ", ["⠐", "⠻"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ゾ", ["⠐", "⠺"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ダ", ["⠐", "⠕"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヂ", ["⠐", "⠗"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヅ", ["⠐", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("デ", ["⠐", "⠟"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ド", ["⠐", "⠞"]) #2026/05/30
        self.append_special_braille_lettr_rules02("バ", ["⠐", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ビ", ["⠐", "⠧"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ブ", ["⠐", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ベ", ["⠐", "⠯"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ボ", ["⠐", "⠮"]) #2026/05/30
        # カタカナ 半濁音
        self.append_special_braille_lettr_rules02("パ", ["⠠", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ピ", ["⠠", "⠧"]) #2026/05/30
        self.append_special_braille_lettr_rules02("プ", ["⠠", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ペ", ["⠠", "⠯"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ポ", ["⠠", "⠮"]) #2026/05/30
        # カタカナ 拗音 (youon)
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_special_braille_lettr_rules02("キャ", ["⠈", "⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("キュ", ["⠈", "⠩"]) #2026/05/30
        self.append_special_braille_lettr_rules02("キョ", ["⠈", "⠪"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ギャ", ["⠘", "⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ギュ", ["⠘", "⠩"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ギョ", ["⠘", "⠪"]) #2026/05/30
        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_special_braille_lettr_rules02("シャ", ["⠈", "⠱"]) #2026/05/30
        self.append_special_braille_lettr_rules02("シュ", ["⠈", "⠹"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ショ", ["⠈", "⠺"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ジャ", ["⠘", "⠱"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ジュ", ["⠘", "⠹"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ジョ", ["⠘", "⠺"]) #2026/05/30
        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_special_braille_lettr_rules02("チャ", ["⠈", "⠕"]) #2026/05/30
        self.append_special_braille_lettr_rules02("チュ", ["⠈", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("チョ", ["⠈", "⠞"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ヂャ", ["⠘", "⠕"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヂュ", ["⠘", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヂョ", ["⠘", "⠞"]) #2026/05/30
        # にゃ にゅ にょ
        self.append_special_braille_lettr_rules02("ニャ", ["⠈", "⠅"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ニュ", ["⠈", "⠍"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ニョ", ["⠈", "⠎"]) #2026/05/30
        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_special_braille_lettr_rules02("ヒャ", ["⠈", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヒュ", ["⠈", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヒョ", ["⠈", "⠮"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ビャ", ["⠘", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ビュ", ["⠘", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ビョ", ["⠘", "⠮"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ピャ", ["⠨", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ピュ", ["⠨", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ピョ", ["⠨", "⠮"]) #2026/05/30
        # みゃ みゅ みょ
        self.append_special_braille_lettr_rules02("ミャ", ["⠈", "⠵"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ミュ", ["⠈", "⠽"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ミョ", ["⠈", "⠾"]) #2026/05/30
        # りゃ りゅ りょ
        self.append_special_braille_lettr_rules02("リャ", ["⠈", "⠑"]) #2026/05/30
        self.append_special_braille_lettr_rules02("リュ", ["⠈", "⠙"]) #2026/05/30
        self.append_special_braille_lettr_rules02("リョ", ["⠈", "⠚"]) #2026/05/30
        #イ段 / ウ段 
        self.append_special_braille_lettr_rules02("イェ", ["⠈", "⠋"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ウィ", ["⠢", "⠃"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ウェ", ["⠢", "⠋"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ウォ", ["⠢", "⠊"]) #2026/05/30
        #キ系
        self.append_special_braille_lettr_rules02("キェ", ["⠈", "⠫"]) #2026/05/30
        #ク系 / グ系
        self.append_special_braille_lettr_rules02("クァ", ["⠢", "⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("クィ", ["⠢", "⠣"]) #2026/05/30
        self.append_special_braille_lettr_rules02("クェ", ["⠢", "⠫"]) #2026/05/30
        self.append_special_braille_lettr_rules02("クォ", ["⠢", "⠪"]) #2026/05/30
        
        self.append_special_braille_lettr_rules02("グァ", ["⠲", "⠡"]) #2026/05/30
        self.append_special_braille_lettr_rules02("グィ", ["⠲", "⠣"]) #2026/05/30
        self.append_special_braille_lettr_rules02("グェ", ["⠲", "⠫"]) #2026/05/30
        self.append_special_braille_lettr_rules02("グォ", ["⠲", "⠪"]) #2026/05/30
        #シ系 / ス系 / ズ系
        self.append_special_braille_lettr_rules02("シェ", ["⠈", "⠻"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ジェ", ["⠘", "⠻"]) #2026/05/30
        self.append_special_braille_lettr_rules02("スィ", ["⠈", "⠳"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ズィ", ["⠘", "⠳"]) #2026/05/30
        #チ系
        self.append_special_braille_lettr_rules02("チェ", ["⠈", "⠟"]) #2026/05/30
        #ツ系
        self.append_special_braille_lettr_rules02("ツァ", ["⠢", "⠕"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ツィ", ["⠢", "⠗"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ツェ", ["⠢", "⠟"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ツォ", ["⠢", "⠞"]) #2026/05/30

        #ティ系 / ディ系 / トゥ系 / ドゥ系
        self.append_special_braille_lettr_rules02("ティ", ["⠈", "⠗"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ディ", ["⠘", "⠗"]) #2026/05/30
        self.append_special_braille_lettr_rules02("テュ", ["⠨", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("デュ", ["⠸", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("トゥ", ["⠢", "⠝"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ドゥ", ["⠲", "⠝"]) #2026/05/30

        #ニェ系 / ヒェ系
        self.append_special_braille_lettr_rules02("ニェ", ["⠈", "⠏"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヒェ", ["⠈", "⠯"]) #2026/05/30

        #F系
        self.append_special_braille_lettr_rules02("ファ", ["⠢", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("フィ", ["⠢", "⠧"]) #2026/05/30
        self.append_special_braille_lettr_rules02("フェ", ["⠢", "⠯"]) #2026/05/30
        self.append_special_braille_lettr_rules02("フォ", ["⠢", "⠮"]) #2026/05/30

        self.append_special_braille_lettr_rules02("フュ", ["⠨", "⠬"]) #2026/05/30
        self.append_special_braille_lettr_rules02("フョ", ["⠨", "⠜"]) #2026/05/30

        #V系
        self.append_special_braille_lettr_rules02("ヴァ", ["⠲", "⠥"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヴィ", ["⠲", "⠧"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヴェ", ["⠲", "⠯"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヴォ", ["⠲", "⠮"]) #2026/05/30

        self.append_special_braille_lettr_rules02("ヴュ", ["⠸", "⠭"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヴョ", ["⠸", "⠮"]) #2026/05/30
        self.append_special_braille_lettr_rules02("ヴ",  ["⠐", "⠉"]) #2026/05/30

        # Katakana small vowels
        self.append_special_braille_lettr_rules02("ァ", ["⠡"])
        self.append_special_braille_lettr_rules02("ィ", ["⠣"])
        self.append_special_braille_lettr_rules02("ゥ", ["⠩"])
        self.append_special_braille_lettr_rules02("ェ", ["⠫"])
        self.append_special_braille_lettr_rules02("ォ", ["⠹"])

        # Katakana small ya/yu/yo
        self.append_special_braille_lettr_rules02("ャ", ["⠈"])
        self.append_special_braille_lettr_rules02("ュ", ["⠊"])
        self.append_special_braille_lettr_rules02("ョ", ["⠌"])

        # カタカナ #促音
        self.append_special_braille_lettr_rules02("ッ", ["⠐"])

        # romanji
        self.append_braille_letter("a", ["⠁"])
        self.append_braille_letter("b", ["⠃"])
        self.append_braille_letter("c", ["⠉"])
        self.append_braille_letter("d", ["⠙"])
        self.append_braille_letter("e", ["⠑"])
        self.append_braille_letter("f", ["⠋"])
        self.append_braille_letter("g", ["⠛"])
        self.append_braille_letter("h", ["⠓"])
        self.append_braille_letter("i", ["⠊"])
        self.append_braille_letter("j", ["⠚"])
        self.append_braille_letter("k", ["⠅"])
        self.append_braille_letter("l", ["⠇"])
        self.append_braille_letter("m", ["⠍"])
        self.append_braille_letter("n", ["⠝"])
        self.append_braille_letter("o", ["⠕"])
        self.append_braille_letter("p", ["⠏"])
        self.append_braille_letter("q", ["⠟"])
        self.append_braille_letter("r", ["⠗"])
        self.append_braille_letter("s", ["⠎"])
        self.append_braille_letter("t", ["⠞"])
        self.append_braille_letter("u", ["⠥"])
        self.append_braille_letter("v", ["⠧"])
        self.append_braille_letter("w", ["⠺"]) 
        self.append_braille_letter("x", ["⠭"])
        self.append_braille_letter("y", ["⠽"])
        self.append_braille_letter("z", ["⠵"])
        
        self.append_special_braille_lettr_rules01("A", ["⠁"])
        self.append_special_braille_lettr_rules01("B", ["⠃"])
        self.append_special_braille_lettr_rules01("C", ["⠉"])
        self.append_special_braille_lettr_rules01("D", ["⠙"])
        self.append_special_braille_lettr_rules01("E", ["⠑"])
        self.append_special_braille_lettr_rules01("F", ["⠋"])
        self.append_special_braille_lettr_rules01("G", ["⠛"])
        self.append_special_braille_lettr_rules01("H", ["⠓"])
        self.append_special_braille_lettr_rules01("I", ["⠊"])
        self.append_special_braille_lettr_rules01("J", ["⠚"])
        self.append_special_braille_lettr_rules01("K", ["⠅"])
        self.append_special_braille_lettr_rules01("L", ["⠇"])
        self.append_special_braille_lettr_rules01("M", ["⠍"])
        self.append_special_braille_lettr_rules01("N", ["⠝"])
        self.append_special_braille_lettr_rules01("O", ["⠕"])
        self.append_special_braille_lettr_rules01("P", ["⠏"])
        self.append_special_braille_lettr_rules01("Q", ["⠟"])
        self.append_special_braille_lettr_rules01("R", ["⠗"])
        self.append_special_braille_lettr_rules01("S", ["⠎"])
        self.append_special_braille_lettr_rules01("T", ["⠞"])
        self.append_special_braille_lettr_rules01("U", ["⠥"])
        self.append_special_braille_lettr_rules01("V", ["⠧"])
        self.append_special_braille_lettr_rules01("W", ["⠺"])
        self.append_special_braille_lettr_rules01("X", ["⠭"])
        self.append_special_braille_lettr_rules01("Y", ["⠽"])
        self.append_special_braille_lettr_rules01("Z", ["⠵"])


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
        self.append_braille_letter("。", ["⠲"]) #2026/05/18
        self.append_braille_letter("、", ["⠰"]) #2026/05/18
        self.append_braille_letter("？", ["⠢"]) #2026/05/18
        self.append_braille_letter("！", ["⠖"]) #2026/05/18
        self.append_braille_letter("・", ["⠐"]) #2026/05/18
        #International
        self.append_braille_letter("?", ["⠢"]) #2026/05/18
        self.append_braille_letter("!", ["⠖"]) #2026/05/18

        #棒線 / 点線
        self.append_braille_letter("―", ["⠒","⠒"]) #2026/05/31
        self.append_braille_letter("…", ["⠂","⠂","⠂"]) #2026/05/31

        #第１カギ / ふたえカギ / 波線 / 第１カッコ / 二重カッコ
        self.append_braille_letter("「", ["⠰", "⠄"]) #2026/05/31
        self.append_braille_letter("」", ["⠠", "⠆"]) #2026/05/31
        self.append_braille_letter("『", ["⠰", "⠤"]) #2026/05/31
        self.append_braille_letter("』", ["⠤", "⠆"]) #2026/05/31
        self.append_braille_letter("～", ["⠤", "⠤"]) #2026/05/31
        self.append_braille_letter("(", ["⠐", "⠶"]) #2026/05/31
        self.append_braille_letter(")", ["⠶", "⠂"]) #2026/05/31
        self.append_braille_letter("((", ["⠰", "⠶"]) #2026/05/31
        self.append_braille_letter("))", ["⠶", "⠆"]) #2026/05/31
        #right / left
        self.append_braille_letter("→", ["⠒", "⠒", "⠕"]) #2026/05/31
        self.append_braille_letter("←", ["⠪", "⠒", "⠒"]) #2026/05/31
        #○ / △ / □ / ×
        self.append_braille_letter("○", ["⠐", "⠵"]) #2026/05/31
        self.append_braille_letter("△", ["⠐", "⠷"]) #2026/05/31
        self.append_braille_letter("□", ["⠐", "⠽"]) #2026/05/31
        self.append_braille_letter("×", ["⠐", "⠿"]) #2026/05/31

        self.append_braille_letter("％", ["⠰", "⠏"]) #2026/05/31
        self.append_braille_letter("＆", ["⠰", "⠯"]) #2026/05/31
        self.append_braille_letter("＠", ["⠰", "⠪"]) #2026/05/31
        self.append_braille_letter("＃", ["⠰", "⠩"]) #2026/05/31
        self.append_braille_letter("＊", ["⠰", "⠡"]) #2026/05/31

        self.append_braille_letter("@", ["⠪"]) #2026/05/31
        self.append_braille_letter("-", ["⠤"]) #2026/05/31
        self.append_braille_letter(".", ["⠲"]) #2026/05/31
        self.append_braille_letter("/", ["⠌"]) #2026/05/31
        self.append_braille_letter(":", ["⠐", "⠂"]) #2026/05/31
        self.append_braille_letter("_", ["⠐", "⠤"]) #2026/05/31
        self.append_braille_letter("~", ["⠐", "⠉"]) #2026/05/31

        self.append_braille_letter("%", ["⠰", "⠏"])
        self.append_braille_letter("&", ["⠰", "⠯"])
        self.append_braille_letter("#", ["⠰", "⠩"])
        self.append_braille_letter("*", ["⠰", "⠡"])




#TEST
#bb = BrailleBaseJapanese()
#print(bb.output_braille_txt("こんにちは！にほんのアニメやゲームは、せかいじゅうでとてもにんきがありますね。こんにちは！にほんのアニメやゲームは、せかいじゅうでとてもにんきがありますね。こんにちは！にほんのアニメやゲームは、せかいじゅうでとてもにんきがありますね。こんにちは！にほんのアニメやゲームは、せかいじゅうでとてもにんきがありますね。"))
