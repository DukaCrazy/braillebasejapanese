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

        self.append_braille_letter("あ", ["⠁"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("い", ["⠃"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("う", ["⠉"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("え", ["⠋"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("お", ["⠊"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("か", ["⠡"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("き", ["⠣"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("く", ["⠩"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("け", ["⠫"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("こ", ["⠪"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("さ", ["⠱"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("し", ["⠳"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("す", ["⠹"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("せ", ["⠻"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("そ", ["⠺"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("た", ["⠕"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ち", ["⠗"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("つ", ["⠝"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("て", ["⠟"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("と", ["⠞"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("な", ["⠅"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("に", ["⠇"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぬ", ["⠍"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ね", ["⠏"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("の", ["⠎"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("は", ["⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひ", ["⠧"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ふ", ["⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("へ", ["⠯"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ほ", ["⠮"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ま", ["⠵"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("み", ["⠷"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("む", ["⠽"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("め", ["⠿"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("も", ["⠾"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("や", ["⠌"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ゆ", ["⠬"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("よ", ["⠜"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ら", ["⠑"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("り", ["⠓"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("る", ["⠙"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("れ", ["⠛"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ろ", ["⠚"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("わ", ["⠄"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ゐ", ["⠰"],2) #2026/05/30
        self.append_braille_letter("ゑ", ["⠲"],2) #2026/05/30
        self.append_braille_letter("を", ["⠔"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ん", ["⠴"],2) #2026/05/18 #2026/05/18
        # 濁音
        self.append_braille_letter("が", ["⠐", "⠡"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎ", ["⠐", "⠣"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぐ", ["⠐", "⠩"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("げ", ["⠐", "⠫"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ご", ["⠐", "⠪"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ざ", ["⠐", "⠱"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("じ", ["⠐", "⠳"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ず", ["⠐", "⠹"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぜ", ["⠐", "⠻"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぞ", ["⠐", "⠺"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("だ", ["⠐", "⠕"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢ", ["⠐", "⠗"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("づ", ["⠐", "⠝"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("で", ["⠐", "⠟"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ど", ["⠐", "⠞"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ば", ["⠐", "⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("び", ["⠐", "⠧"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぶ", ["⠐", "⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("べ", ["⠐", "⠯"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぼ", ["⠐", "⠮"],2) #2026/05/18 #2026/05/18
        # 半濁音
        self.append_braille_letter("ぱ", ["⠠", "⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴ", ["⠠", "⠧"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぷ", ["⠠", "⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぺ", ["⠠", "⠯"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぽ", ["⠠", "⠮"],2) #2026/05/18 #2026/05/18
        #拗音
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_braille_letter("きゃ", ["⠈", "⠡"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("きゅ", ["⠈", "⠩"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("きょ", ["⠈", "⠪"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぎゃ", ["⠘", "⠡"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎゅ", ["⠘", "⠩"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぎょ", ["⠘", "⠪"],2) #2026/05/18 #2026/05/18

        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_braille_letter("しゃ", ["⠈", "⠱"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("しゅ", ["⠈", "⠹"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("しょ", ["⠈", "⠺"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("じゃ", ["⠘", "⠱"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("じゅ", ["⠘", "⠹"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("じょ", ["⠘", "⠺"],2) #2026/05/18 #2026/05/18

        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_braille_letter("ちゃ", ["⠈", "⠕"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ちゅ", ["⠈", "⠝"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ちょ", ["⠈", "⠞"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぢゃ", ["⠘", "⠕"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢゅ", ["⠘", "⠝"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぢょ", ["⠘", "⠞"],2) #2026/05/18 #2026/05/18

        # にゃ にゅ にょ
        self.append_braille_letter("にゃ", ["⠈", "⠅"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("にゅ", ["⠈", "⠍"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("にょ", ["⠈", "⠎"],2) #2026/05/18 #2026/05/18

        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_braille_letter("ひゃ", ["⠈", "⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひゅ", ["⠈", "⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ひょ", ["⠈", "⠮"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("びゃ", ["⠘", "⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("びゅ", ["⠘", "⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("びょ", ["⠘", "⠮"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぴゃ", ["⠨", "⠥"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴゅ", ["⠨", "⠭"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("ぴょ", ["⠨", "⠮"],2) #2026/05/18 #2026/05/18

        # みゃ みゅ みょ
        self.append_braille_letter("みゃ", ["⠈", "⠵"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("みゅ", ["⠈", "⠽"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("みょ", ["⠈", "⠾"],2) #2026/05/18 #2026/05/18

        # りゃ りゅ りょ
        self.append_braille_letter("りゃ", ["⠈", "⠑"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("りゅ", ["⠈", "⠙"],2) #2026/05/18 #2026/05/18
        self.append_braille_letter("りょ", ["⠈", "⠚"],2) #2026/05/18 #2026/05/18

        self.append_braille_letter("ぁ", ["⠡"],2)
        self.append_braille_letter("ぃ", ["⠣"],2)
        self.append_braille_letter("ぅ", ["⠩"],2)
        self.append_braille_letter("ぇ", ["⠫"],2)
        self.append_braille_letter("ぉ", ["⠹"],2)

        self.append_braille_letter("ゃ", ["⠈"],2)
        self.append_braille_letter("ゅ", ["⠊"],2)
        self.append_braille_letter("ょ", ["⠌"],2)
        #促音
        self.append_braille_letter("っ", ["⠂"],2) #2026/05/18 2026/06/08
        #長音 
        self.append_braille_letter("ー", ["⠒"],2) #2026/05/18

        # カタカナ
        self.append_braille_letter("ア", ["⠁"],2) #2026/05/30
        self.append_braille_letter("イ", ["⠃"],2) #2026/05/30
        self.append_braille_letter("ウ", ["⠉"],2) #2026/05/30
        self.append_braille_letter("エ", ["⠋"],2) #2026/05/30
        self.append_braille_letter("オ", ["⠊"],2) #2026/05/30
        self.append_braille_letter("カ", ["⠡"],2) #2026/05/30
        self.append_braille_letter("キ", ["⠣"],2) #2026/05/30
        self.append_braille_letter("ク", ["⠩"],2) #2026/05/30
        self.append_braille_letter("ケ", ["⠫"],2) #2026/05/30
        self.append_braille_letter("コ", ["⠪"],2) #2026/05/30
        self.append_braille_letter("サ", ["⠱"],2) #2026/05/30
        self.append_braille_letter("シ", ["⠳"],2) #2026/05/30
        self.append_braille_letter("ス", ["⠹"],2) #2026/05/30
        self.append_braille_letter("セ", ["⠻"],2) #2026/05/30
        self.append_braille_letter("ソ", ["⠺"],2) #2026/05/30
        self.append_braille_letter("タ", ["⠕"],2) #2026/05/30
        self.append_braille_letter("チ", ["⠗"],2) #2026/05/30
        self.append_braille_letter("ツ", ["⠝"],2) #2026/05/30
        self.append_braille_letter("テ", ["⠟"],2) #2026/05/30
        self.append_braille_letter("ト", ["⠞"],2) #2026/05/30
        self.append_braille_letter("ナ", ["⠅"],2) #2026/05/30
        self.append_braille_letter("ニ", ["⠇"],2) #2026/05/30
        self.append_braille_letter("ヌ", ["⠍"],2) #2026/05/30
        self.append_braille_letter("ネ", ["⠏"],2) #2026/05/30
        self.append_braille_letter("ノ", ["⠎"],2) #2026/05/30
        self.append_braille_letter("ハ", ["⠥"],2) #2026/05/30
        self.append_braille_letter("ヒ", ["⠧"],2) #2026/05/30
        self.append_braille_letter("フ", ["⠭"],2) #2026/05/30
        self.append_braille_letter("ヘ", ["⠯"],2) #2026/05/30
        self.append_braille_letter("ホ", ["⠮"],2) #2026/05/30
        self.append_braille_letter("マ", ["⠵"],2) #2026/05/30
        self.append_braille_letter("ミ", ["⠷"],2) #2026/05/30
        self.append_braille_letter("ム", ["⠽"],2) #2026/05/30
        self.append_braille_letter("メ", ["⠿"],2) #2026/05/30
        self.append_braille_letter("モ", ["⠾"],2) #2026/05/30
        self.append_braille_letter("ヤ", ["⠌"],2) #2026/05/30
        self.append_braille_letter("ユ", ["⠬"],2) #2026/05/30
        self.append_braille_letter("ヨ", ["⠜"],2) #2026/05/30
        self.append_braille_letter("ラ", ["⠑"],2) #2026/05/30
        self.append_braille_letter("リ", ["⠓"],2) #2026/05/30
        self.append_braille_letter("ル", ["⠙"],2) #2026/05/30
        self.append_braille_letter("レ", ["⠛"],2) #2026/05/30
        self.append_braille_letter("ロ", ["⠚"],2) #2026/05/30
        self.append_braille_letter("ワ", ["⠄"],2) #2026/05/30
        self.append_braille_letter("ヰ", ["⠰"],2) #2026/05/30
        self.append_braille_letter("ヱ", ["⠲"],2) #2026/05/30
        self.append_braille_letter("ヲ", ["⠔"],2) #2026/05/30
        self.append_braille_letter("ン", ["⠴"],2) #2026/05/30
        # カタカナ 濁音
        self.append_braille_letter("ガ", ["⠐", "⠡"],2) #2026/05/30
        self.append_braille_letter("ギ", ["⠐", "⠣"],2) #2026/05/30
        self.append_braille_letter("グ", ["⠐", "⠩"],2) #2026/05/30
        self.append_braille_letter("ゲ", ["⠐", "⠫"],2) #2026/05/30
        self.append_braille_letter("ゴ", ["⠐", "⠪"],2) #2026/05/30
        self.append_braille_letter("ザ", ["⠐", "⠱"],2) #2026/05/30
        self.append_braille_letter("ジ", ["⠐", "⠳"],2) #2026/05/30
        self.append_braille_letter("ズ", ["⠐", "⠹"],2) #2026/05/30
        self.append_braille_letter("ゼ", ["⠐", "⠻"],2) #2026/05/30
        self.append_braille_letter("ゾ", ["⠐", "⠺"],2) #2026/05/30
        self.append_braille_letter("ダ", ["⠐", "⠕"],2) #2026/05/30
        self.append_braille_letter("ヂ", ["⠐", "⠗"],2) #2026/05/30
        self.append_braille_letter("ヅ", ["⠐", "⠝"],2) #2026/05/30
        self.append_braille_letter("デ", ["⠐", "⠟"],2) #2026/05/30
        self.append_braille_letter("ド", ["⠐", "⠞"],2) #2026/05/30
        self.append_braille_letter("バ", ["⠐", "⠥"],2) #2026/05/30
        self.append_braille_letter("ビ", ["⠐", "⠧"],2) #2026/05/30
        self.append_braille_letter("ブ", ["⠐", "⠭"],2) #2026/05/30
        self.append_braille_letter("ベ", ["⠐", "⠯"],2) #2026/05/30
        self.append_braille_letter("ボ", ["⠐", "⠮"],2) #2026/05/30
        # カタカナ 半濁音
        self.append_braille_letter("パ", ["⠠", "⠥"],2) #2026/05/30
        self.append_braille_letter("ピ", ["⠠", "⠧"],2) #2026/05/30
        self.append_braille_letter("プ", ["⠠", "⠭"],2) #2026/05/30
        self.append_braille_letter("ペ", ["⠠", "⠯"],2) #2026/05/30
        self.append_braille_letter("ポ", ["⠠", "⠮"],2) #2026/05/30
        # カタカナ 拗音 (youon)
        # きゃ きゅ きょ / ぎゃ ぎゅ ぎょ
        self.append_braille_letter("キャ", ["⠈", "⠡"],2) #2026/05/30
        self.append_braille_letter("キュ", ["⠈", "⠩"],2) #2026/05/30
        self.append_braille_letter("キョ", ["⠈", "⠪"],2) #2026/05/30

        self.append_braille_letter("ギャ", ["⠘", "⠡"],2) #2026/05/30
        self.append_braille_letter("ギュ", ["⠘", "⠩"],2) #2026/05/30
        self.append_braille_letter("ギョ", ["⠘", "⠪"],2) #2026/05/30
        # しゃ しゅ しょ / じゃ じゅ じょ
        self.append_braille_letter("シャ", ["⠈", "⠱"],2) #2026/05/30
        self.append_braille_letter("シュ", ["⠈", "⠹"],2) #2026/05/30
        self.append_braille_letter("ショ", ["⠈", "⠺"],2) #2026/05/30

        self.append_braille_letter("ジャ", ["⠘", "⠱"],2) #2026/05/30
        self.append_braille_letter("ジュ", ["⠘", "⠹"],2) #2026/05/30
        self.append_braille_letter("ジョ", ["⠘", "⠺"],2) #2026/05/30
        # ちゃ ちゅ ちょ / ぢゃ ぢゅ ぢょ
        self.append_braille_letter("チャ", ["⠈", "⠕"],2) #2026/05/30
        self.append_braille_letter("チュ", ["⠈", "⠝"],2) #2026/05/30
        self.append_braille_letter("チョ", ["⠈", "⠞"],2) #2026/05/30

        self.append_braille_letter("ヂャ", ["⠘", "⠕"],2) #2026/05/30
        self.append_braille_letter("ヂュ", ["⠘", "⠝"],2) #2026/05/30
        self.append_braille_letter("ヂョ", ["⠘", "⠞"],2) #2026/05/30
        # にゃ にゅ にょ
        self.append_braille_letter("ニャ", ["⠈", "⠅"],2) #2026/05/30
        self.append_braille_letter("ニュ", ["⠈", "⠍"],2) #2026/05/30
        self.append_braille_letter("ニョ", ["⠈", "⠎"],2) #2026/05/30
        # ひゃ ひゅ ひょ / びゃ びゅ びょ / ぴゃ ぴゅ ぴょ
        self.append_braille_letter("ヒャ", ["⠈", "⠥"],2) #2026/05/30
        self.append_braille_letter("ヒュ", ["⠈", "⠭"],2) #2026/05/30
        self.append_braille_letter("ヒョ", ["⠈", "⠮"],2) #2026/05/30

        self.append_braille_letter("ビャ", ["⠘", "⠥"],2) #2026/05/30
        self.append_braille_letter("ビュ", ["⠘", "⠭"],2) #2026/05/30
        self.append_braille_letter("ビョ", ["⠘", "⠮"],2) #2026/05/30

        self.append_braille_letter("ピャ", ["⠨", "⠥"],2) #2026/05/30
        self.append_braille_letter("ピュ", ["⠨", "⠭"],2) #2026/05/30
        self.append_braille_letter("ピョ", ["⠨", "⠮"],2) #2026/05/30
        # みゃ みゅ みょ
        self.append_braille_letter("ミャ", ["⠈", "⠵"],2) #2026/05/30
        self.append_braille_letter("ミュ", ["⠈", "⠽"],2) #2026/05/30
        self.append_braille_letter("ミョ", ["⠈", "⠾"],2) #2026/05/30
        # りゃ りゅ りょ
        self.append_braille_letter("リャ", ["⠈", "⠑"],2) #2026/05/30
        self.append_braille_letter("リュ", ["⠈", "⠙"],2) #2026/05/30
        self.append_braille_letter("リョ", ["⠈", "⠚"],2) #2026/05/30

        #イ段 / ウ段 Special
        self.append_braille_letter("イェ", ["⠈", "⠋"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ウィ", ["⠢", "⠃"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ウェ", ["⠢", "⠋"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ウォ", ["⠢", "⠊"],2) #2026/05/30 2026/06/08
        #キ系
        self.append_braille_letter("キェ", ["⠈", "⠫"],2) #2026/05/30 2026/06/08
        #ク系 / グ系
        self.append_braille_letter("クァ", ["⠢", "⠡"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("クィ", ["⠢", "⠣"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("クェ", ["⠢", "⠫"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("クォ", ["⠢", "⠪"],2) #2026/05/30 2026/06/08
        
        self.append_braille_letter("グァ", ["⠲", "⠡"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("グィ", ["⠲", "⠣"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("グェ", ["⠲", "⠫"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("グォ", ["⠲", "⠪"],2) #2026/05/30 2026/06/08
        #シ系 / ス系 / ズ系
        self.append_braille_letter("シェ", ["⠈", "⠻"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ジェ", ["⠘", "⠻"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("スィ", ["⠈", "⠳"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ズィ", ["⠘", "⠳"],2) #2026/05/30 2026/06/08
        #チ系
        self.append_braille_letter("チェ", ["⠈", "⠟"],2) #2026/05/30 2026/06/08
        #ツ系
        self.append_braille_letter("ツァ", ["⠢", "⠕"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ツィ", ["⠢", "⠗"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ツェ", ["⠢", "⠟"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ツォ", ["⠢", "⠞"],2) #2026/05/30 2026/06/08

        #ティ系 / ディ系 / トゥ系 / ドゥ系
        self.append_braille_letter("ティ", ["⠈", "⠗"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ディ", ["⠘", "⠗"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("テュ", ["⠨", "⠝"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("デュ", ["⠸", "⠝"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("トゥ", ["⠢", "⠝"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ドゥ", ["⠲", "⠝"],2) #2026/05/30 2026/06/08

        #ニェ系 / ヒェ系
        self.append_braille_letter("ニェ", ["⠈", "⠏"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヒェ", ["⠈", "⠯"],2) #2026/05/30 2026/06/08

        #F系
        self.append_braille_letter("ファ", ["⠢", "⠥"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("フィ", ["⠢", "⠧"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("フェ", ["⠢", "⠯"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("フォ", ["⠢", "⠮"],2) #2026/05/30 2026/06/08

        self.append_braille_letter("フュ", ["⠨", "⠬"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("フョ", ["⠨", "⠜"],2) #2026/05/30 2026/06/08

        #V系
        self.append_braille_letter("ヴァ", ["⠲", "⠥"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヴィ", ["⠲", "⠧"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヴェ", ["⠲", "⠯"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヴォ", ["⠲", "⠮"],2) #2026/05/30 2026/06/08

        self.append_braille_letter("ヴュ", ["⠸", "⠭"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヴョ", ["⠸", "⠮"],2) #2026/05/30 2026/06/08
        self.append_braille_letter("ヴ",  ["⠐", "⠉"],2) #2026/05/30 2026/06/08

        # Katakana small vowels
        self.append_braille_letter("ァ", ["⠡"],2)
        self.append_braille_letter("ィ", ["⠣"],2)
        self.append_braille_letter("ゥ", ["⠩"],2)
        self.append_braille_letter("ェ", ["⠫"],2)
        self.append_braille_letter("ォ", ["⠹"],2)

        # Katakana small ya/yu/yo
        self.append_braille_letter("ャ", ["⠈"],2)
        self.append_braille_letter("ュ", ["⠊"],2)
        self.append_braille_letter("ョ", ["⠌"],2)

        # カタカナ #促音
        self.append_braille_letter("ッ", ["⠂"],2) #2026/06/08

        # romanji
        self.append_braille_letter("外字", ["⠰"]) #2026/06/08 #Temporary
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
        
        self.append_braille_letter("A", ["⠁"],1) #2026/06/08
        self.append_braille_letter("B", ["⠃"],1) #2026/06/08
        self.append_braille_letter("C", ["⠉"],1) #2026/06/08
        self.append_braille_letter("D", ["⠙"],1) #2026/06/08
        self.append_braille_letter("E", ["⠑"],1) #2026/06/08
        self.append_braille_letter("F", ["⠋"],1) #2026/06/08
        self.append_braille_letter("G", ["⠛"],1) #2026/06/08
        self.append_braille_letter("H", ["⠓"],1) #2026/06/08
        self.append_braille_letter("I", ["⠊"],1) #2026/06/08
        self.append_braille_letter("J", ["⠚"],1) #2026/06/08
        self.append_braille_letter("K", ["⠅"],1) #2026/06/08
        self.append_braille_letter("L", ["⠇"],1) #2026/06/08
        self.append_braille_letter("M", ["⠍"],1) #2026/06/08
        self.append_braille_letter("N", ["⠝"],1) #2026/06/08
        self.append_braille_letter("O", ["⠕"],1) #2026/06/08
        self.append_braille_letter("P", ["⠏"],1) #2026/06/08
        self.append_braille_letter("Q", ["⠟"],1) #2026/06/08
        self.append_braille_letter("R", ["⠗"],1) #2026/06/08
        self.append_braille_letter("S", ["⠎"],1) #2026/06/08
        self.append_braille_letter("T", ["⠞"],1) #2026/06/08
        self.append_braille_letter("U", ["⠥"],1) #2026/06/08
        self.append_braille_letter("V", ["⠧"],1) #2026/06/08
        self.append_braille_letter("W", ["⠺"],1) #2026/06/08
        self.append_braille_letter("X", ["⠭"],1) #2026/06/08
        self.append_braille_letter("Y", ["⠽"],1) #2026/06/08
        self.append_braille_letter("Z", ["⠵"],1) #2026/06/08


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
        self.append_braille_letter("。", ["⠲", "⠀"],2) #2026/05/18 #2026/06/14
        self.append_braille_letter("、", ["⠰", "⠀"],2) #2026/05/18 #2026/06/14
        self.append_braille_letter("？", ["⠢", "⠀"],2) #2026/05/18 #2026/06/14
        self.append_braille_letter("！", ["⠖", "⠀"],2) #2026/05/18 #2026/06/14
        self.append_braille_letter("・", ["⠐", "⠀"],2) #2026/05/18 #2026/06/14
        self.append_braille_letter(":", ["⠐", "⠂", "⠀"],2) #2026/05/31  #2026/06/08 #2026/06/14
        #International
        self.append_braille_letter("?", ["⠢", "⠀"],2) #2026/05/18
        self.append_braille_letter("!", ["⠖", "⠀"],2) #2026/05/18

        #棒線 / 点線
        self.append_braille_letter("―", ["⠒","⠒"]) #2026/05/31
        self.append_braille_letter("…", ["⠂","⠂","⠂"]) #2026/05/31

        #第１カギ / ふたえカギ / 波線 / 第１カッコ / 二重カッコ
        self.append_braille_letter("「", ["⠰", "⠄"],2) #2026/05/31
        self.append_braille_letter("」", ["⠠", "⠆"],2) #2026/05/31
        self.append_braille_letter("『", ["⠰", "⠤"],2) #2026/05/31
        self.append_braille_letter("』", ["⠤", "⠆"],2) #2026/05/31
        self.append_braille_letter("～", ["⠤", "⠤"],2) #2026/05/31
        self.append_braille_letter("(", ["⠐", "⠶"],2) #2026/05/31
        self.append_braille_letter(")", ["⠶", "⠂"],2) #2026/05/31
        self.append_braille_letter("((", ["⠰", "⠶"],2) #2026/05/31
        self.append_braille_letter("))", ["⠶", "⠆"],2) #2026/05/31
        #right / left
        self.append_braille_letter("→", ["⠒", "⠒", "⠕"],2) #2026/05/31
        self.append_braille_letter("←", ["⠪", "⠒", "⠒"],2) #2026/05/31
        #○ / △ / □ / ×
        self.append_braille_letter("○", ["⠐", "⠵"],2) #2026/05/31
        self.append_braille_letter("△", ["⠐", "⠷"],2) #2026/05/31
        self.append_braille_letter("□", ["⠐", "⠽"],2) #2026/05/31
        self.append_braille_letter("×", ["⠐", "⠿"],2) #2026/05/31

        self.append_braille_letter("％", ["⠰", "⠏"],2) #2026/05/31
        self.append_braille_letter("   ", ["⠰", "⠯"],2) #2026/05/31
        self.append_braille_letter("＠", ["⠰", "⠪"],2) #2026/05/31
        self.append_braille_letter("＃", ["⠰", "⠩"],2) #2026/05/31
        self.append_braille_letter("＊", ["⠰", "⠡"],2) #2026/05/31

        self.append_braille_letter("@", ["⠪"],2) #2026/05/31
        self.append_braille_letter("-", ["⠤"],2) #2026/05/31
        self.append_braille_letter(".", ["⠲"],2) #2026/05/31
        self.append_braille_letter(",", ["⠂"],2) #2026/06/08
        self.append_braille_letter("/", ["⠌"],2) #2026/05/31 
        self.append_braille_letter(";", ["⠆"],2) #2026/06/08
        self.append_braille_letter("'", ["⠄"],2) #2026/06/08

        self.append_braille_letter("_", ["⠐", "⠤"],2) #2026/05/31
        self.append_braille_letter("~", ["⠐", "⠉"],2) #2026/05/31

        self.append_braille_letter("%", ["⠰", "⠏"],2)
        self.append_braille_letter("&", ["⠈", "⠯"],2) #2026/06/08
        self.append_braille_letter("#", ["⠰", "⠩"],2)
        self.append_braille_letter("*", ["⠰", "⠡"],2)
