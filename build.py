# 6畳ラボのサイトを作る。articles の中身から HTML を書き出し、図を縮小して img/ に置く。
import os, html, datetime
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
PINS = os.path.join(os.path.dirname(ROOT), "pins")
ICON = os.path.join(os.path.dirname(ROOT), "icon_6jolab_room.png")
BASE = "https://kame6493-del.github.io/6jo-lab/"
TODAY = datetime.date.today()
ROOM = "https://room.rakuten.co.jp/room_1c124220fb/items"

os.makedirs(os.path.join(OUT, "img"), exist_ok=True)

def save_images(src, slug):
    im = Image.open(os.path.join(PINS, src)).convert("RGB")
    full = im.copy(); full.thumbnail((900, 1350))
    full.save(os.path.join(OUT, "img", slug + ".jpg"), "JPEG", quality=85, optimize=True)
    w, h = im.size
    th = im.crop((0, 0, w, int(w * 0.72))); th.thumbnail((640, 460))
    th.save(os.path.join(OUT, "img", slug + "-thumb.jpg"), "JPEG", quality=82, optimize=True)

if os.path.exists(ICON):
    ic = Image.open(ICON).convert("RGB"); ic.thumbnail((96, 96)); ic.save(os.path.join(OUT, "img", "icon.png"))

# 本文: 文字列は段落、("h", 見出し)は小見出し。pr は (説明, URL) の並び
articles = [
  dict(slug="rug-size", pin="pin_6jo_rug.png", tag="ラグ",
    title="6畳のラグ、何cmにするか問題",
    lede="ラグって、色より先に大きさで失敗するんですよね。",
    desc="6畳に置くラグの大きさの目安。ベッドがある部屋なら130×185cm前後、ベッドがない部屋なら185×185cm前後。床を少し残すと広く見えます。",
    body=[
      "6畳の部屋に置くなら、目安はわりとはっきりしていて、ベッドがある部屋なら130×185cmくらい(約1.5畳)、ベッドがない部屋なら185×185cmくらい(約2畳)です。",
      "ベッドがあると、床で自由に使えるのはベッドの横のひと区画くらいになります。そこに収まるのが130×185cm。ベッドを置かずにローテーブルで暮らすなら、座る場所ごと敷ける185×185cmがちょうどいい大きさです。",
      "やりがちなのが、床が見えなくなるくらい大きいものを選んでしまうこと。6畳だと、ラグのまわりに床が少し見えているほうが部屋は広く見えます。図の200×250cmになると、6畳ではほとんど床が埋まってしまいます。",
      "置く前に、床にマスキングテープで大きさを貼ってみるのがおすすめです。ベッドや机の脚がどこに乗るかも、そこで分かります。",
      "冬に使うなら、洗えるかどうかも見ておきたいところです。ラグの上で食べたり寝転んだりする時間は長いので、洗濯機に入るかどうかで、何年使えるかが変わってきます。",
    ],
    pr=[("130×185cmと185×185cmがあって、洗えるフランネルのラグ", "https://a.r10.to/hFh9AF")]),
  dict(slug="curtain-size", pin="pin_curtain.png", tag="カーテン",
    title="カーテンは、窓じゃなくてレールを測る",
    lede="窓を測って買ったら、届いたカーテンが短かった。よくある失敗です。",
    desc="カーテンの幅はレールの固定ランナーの間×1.05、丈は掃き出し窓ならランナーの下から床まで−1cm、腰窓なら窓枠の下+15〜20cm。",
    body=[
      "カーテンの寸法は、窓ではなくレールが基準になります。幅は、レールの両端にある動かない輪(固定ランナー)の間を測って、1.05倍。少しゆとりを持たせないと、閉めたときに端がすいてしまいます。両開きなら、その半分の幅を2枚です。",
      "丈は、窓の形で測り方が変わります。床まである掃き出し窓なら、ランナー(フックを掛ける輪)の下から床までを測って、1cm引きます。床に付くと裾が汚れやすいし、短いと下から光がもれます。",
      "腰の高さの窓なら、ランナーの下から窓枠の下までを測って、15〜20cm足します。窓枠より下まで隠れるようにしておくと、すき間風も光もれも減ります。",
      "冬のことを考えるなら、腰窓は気持ち長めがいいと思います。窓で冷えた空気は下へ落ちてくるので、丈が短いと、そのまま部屋に入ってきてしまうんです。",
    ],
    pr=[("丈は1cm単位、幅は5cm単位で頼める1級遮光カーテン(日本製・洗える)", "https://a.r10.to/hPsTgB")]),
  dict(slug="winter-futon", pin="pin_fuyu_futon.png", tag="寝具",
    title="冬の布団が寒いとき、足すのは下から",
    lede="布団が寒いと掛け布団を厚くしたくなるんですが、寒さは下から来ていることが多いんです。",
    desc="冬の寝具は下から足すのが目安。敷きパッドを冬用に、掛け布団と体の間に毛布、それでも寒ければ掛け布団を冬用に。",
    body=[
      "敷き布団やマットレスは、床の冷たさを直接受けています。なので、足していく順番は、まず敷きパッドを起毛の冬用に替えるところから。次に、掛け布団と体のあいだに毛布を1枚。それでも寒ければ、そこで初めて掛け布団を冬用にします。",
      "下を先に暖かくしておくと、同じ掛け布団でも寒さの感じ方がかなり変わります。",
      "6畳でベッドを置かず、床に布団を敷いて寝ている人は、床からの冷えがさらに強くなります。布団の下にラグを1枚敷いておくだけでも、冷たさはやわらぎます。",
    ],
    pr=[("冬用の敷きパッド。洗濯機で洗えて、シングルからある", "https://a.r10.to/hgG3qt"),
        ("洗濯機で洗えて、シングルからある毛布", "https://a.r10.to/hFOkGj")]),
  dict(slug="moufu", pin="pin_moufu.png", tag="寝具",
    title="毛布を選ぶなら、まず洗えるかどうか",
    lede="毛布って種類が多くて、どれも暖かそうに見えるんですよね。",
    desc="毛布を選ぶときは、洗濯機で洗えるか、サイズ(シングルは140×200cm前後)、素材の順に見ると絞れます。",
    body=[
      "一人暮らしなら、最初に見るのは洗濯機で洗えるかどうかだと思います。大きな寝具を毎回クリーニングに出すのは、正直なかなか続きません。洗濯表示で、桶のマークに×が付いていなければ、家で洗えます。",
      "サイズは、シングルなら140×200cm前後が多いです。ベッドの幅より少し大きいと、寝返りをしてもはみ出しにくくなります。",
      "素材は手触りの好みですが、ふわっとしたものはポリエステルのマイクロファイバー系が多いです。軽くて乾きやすいので、洗う前提ならこれが楽です。",
    ],
    pr=[("洗濯機で洗えて、シングル・セミダブル・ダブルがある毛布", "https://a.r10.to/hFOkGj")]),
  dict(slug="mattress", pin="pin_mattress.png", tag="寝具",
    title="マットレスを床に直置きするなら、湿気だけは気にしておく",
    lede="ベッドを置かないと、6畳でも床がかなり空きます。そのかわり気になるのが湿気です。",
    desc="6畳でマットレスを床に直置きするなら、下にこもる湿気に注意。すのこを挟む、三つ折りを朝たたんで立てる、の組み合わせが手軽です。",
    body=[
      "寝ている間の汗は、下へ抜けにくいんです。床とマットレスのあいだにこもって、敷きっぱなしだと乾く時間がありません。",
      "手軽なのは、すのこを1枚挟むこと。すき間から空気が通るので、湿気が抜けやすくなります。",
      "三つ折りのマットレスなら、朝たたんで立てておくのもいいです。床が空くし、マットレスの下も乾く。掃除もしやすくなります。ベッドなしの6畳だと、この2つを組み合わせるのがいちばん手軽だと思います。",
    ],
    pr=[("三つ折りで、シングルは97×195cm。厚さは10cmと5cm、カバーを外して洗える", "https://a.r10.to/hgCGkU")]),
  dict(slug="mado-reiki", pin="pin_mado_reiki.png", tag="冬支度",
    title="冬の窓際が寒いのは、冷気が落ちてくるから",
    lede="窓の近くにいると、足元だけすうっと冷える。あれにはちゃんと理由があります。",
    desc="冬に窓際が寒いのは、ガラスで冷えた空気が床へ落ちてくるから。カーテンの丈、断熱パネル、寝る場所の位置で、賃貸でも対策できます。",
    body=[
      "窓のガラスで冷やされた空気は、重くなって窓に沿って下へ落ちます。それが床を這って部屋に広がるので、足元から冷えるんです。",
      "賃貸でもできることでいうと、まずカーテンを床まで届く長さにすること。下のすき間から冷気が出にくくなります。窓の下に断熱パネルを立てるのも効きます。置くだけのものや、はがせるものなら、原状回復の心配も少なくて済みます。",
      "地味に効くのが、寝る場所を窓から少し離すことです。6畳だとベッドと窓が近くなりがちなので、配置を考えるときに窓との距離も入れておくと、冬がだいぶ楽になります。",
    ],
    pr=[("6畳の冬支度に使える毛布・布団・ラグをまとめた楽天ROOM", "https://room.rakuten.co.jp/room_1c124220fb/collection/1800012748397273")]),
  dict(slug="taikyo", pin="pin_taikyo.png", tag="賃貸",
    title="退去費用、どこまで払うのか",
    lede="賃貸を出るときに気になるのが、どこまでが自分の負担になるのか、ですよね。",
    desc="国交省の原状回復ガイドラインでは、家具の跡や画びょうの穴、日焼けはふつうに暮らしてできたもの。ネジ穴やタバコのヤニは借りた人の負担になりやすい。",
    body=[
      "ひとつの目安になるのが、国土交通省の「原状回復をめぐるトラブルとガイドライン」です。",
      "家具を置いていた床のへこみ、画びょうやピンの穴、日焼けによる壁紙の色あせ。こういうものは、ふつうに暮らしていればできるものとして扱われています。",
      "逆に、タバコのヤニや臭い、壁に開けたネジ穴、手入れをせずに広がったカビなどは、借りた人の負担になりやすいとされています。",
      "なので、棚や収納を壁に付けるなら、ネジではなくピンで留めるものか、突っ張り式のものにしておくと安心です。ただ、契約書に特約が書かれていることもあるので、そこは先に確かめておいてください。",
      "それと、入居した日に床や壁の傷を写真に撮っておくと、退去のときに説明しやすくなります。今からでも、これから付く傷との区別には使えます。",
    ],
    pr=[("ピンや突っ張りで付けられる、壁に穴を残しにくい収納をまとめた楽天ROOM", "https://room.rakuten.co.jp/room_1c124220fb/collection/1800012748348292")]),
  dict(slug="denki-moufu", pin="pin_denki_moufu.png", tag="冬支度",
    title="電気毛布は、敷くか掛けるかで選ぶ",
    lede="電気毛布って、敷くタイプと掛けるタイプがあるんですよね。",
    desc="電気毛布は、床の冷えが気になるなら敷くタイプ、肩や足先が冷えるなら掛けるタイプ。迷ったら敷き掛け両用。寝るときは切るか弱が目安。",
    body=[
      "どちらがいいかは、どこが冷えるかで決まります。床からの冷えが気になるなら、体の下から温める敷くタイプ。肩や足先が冷えるなら、上から包む掛けるタイプです。",
      "6畳でベッドを置かずに床に布団を敷いているなら、床の冷たさを直接受けるので、敷くタイプのほうが効きやすいと思います。迷ったら、どちらにも使える敷き掛け両用にしておくと、季節や寝方で入れ替えられます。",
      "使い方の目安は、寝る前に温めておいて、眠るときは切るか弱にすること。それと、コントローラーを外して本体を丸洗いできるかどうかは、買う前に見ておくと後が楽です。",
    ],
    pr=[("敷き掛け両用で、本体を丸洗いできる電気毛布(190×130・160×80・120×60cm)", "https://a.r10.to/h8spgD")]),
  dict(slug="kotatsu", pin="pin_kotatsu.png", tag="冬支度",
    title="6畳にこたつを置くなら、布団を広げた大きさで測る",
    lede="こたつは天板の大きさで選びがちですが、場所をとるのは布団のほうなんです。",
    desc="6畳に置くこたつは、天板60×60cmの一人用なら布団は約160cm角でベッドの横に収まる。75×75cmだと布団は約180cm角でほぼいっぱい。",
    body=[
      "こたつ布団は、天板より片側50cmほどずつ広がるのが目安です。天板60×60cmの一人用なら、布団は160cm角くらい。75×75cmなら180cm角くらいになります。",
      "6畳(江戸間で261×352cmくらい)にシングルベッドを置いている部屋だと、一人用ならベッドの横に収まります。75×75cmになると、ベッドと並べたときに床がほとんど残りません。",
      "なので、測るときは天板ではなく、布団を広げた大きさで床を測っておくのがおすすめです。夏は布団を外せば、そのままローテーブルとして使えます。",
    ],
    pr=[("天板60×60cmの一人用こたつと布団のセット", "https://a.r10.to/h5ldHu")]),
  dict(slug="kashitsuki", pin="pin_kashitsuki.png", tag="冬支度",
    title="加湿器は、窓と壁から離して部屋の真ん中寄りに",
    lede="加湿器を窓のそばに置くと、朝、窓がびっしょりになることがあります。",
    desc="加湿器は窓の近くだと結露しやすく、壁ぎわだと壁紙が湿ってカビの原因に。部屋の真ん中寄りで、台の上など床から少し高い所に置くのが目安。",
    body=[
      "冷えた窓ガラスのそばで加湿すると、湿気がガラスで水滴になって結露しやすくなります。壁ぎわも同じで、壁紙が湿るとカビの原因になります。",
      "置くなら、窓と壁から少し離した部屋の真ん中寄り。床に直接置くより、台の上など少し高い所に置いたほうが、部屋全体に広がりやすいです。",
      "選ぶときは、箱や商品ページに書いてある適用畳数を見ておきます。木造和室とプレハブ洋室の2つが書いてあることが多く、マンションの洋室ならプレハブ洋室の数字が6畳以上あるかを見ればいいです。",
    ],
    pr=[("タンク6Lのハイブリッド式加湿器", "https://a.r10.to/hYgP7e")]),
]

CSS = """:root{--bg:#fff;--ink:#333;--sub:#777;--line:#e8e8e8;--soft:#f7f7f5;--link:#2a6496;--acc:#3e6b57}
@media (prefers-color-scheme:dark){:root{--bg:#1b1b1b;--ink:#ddd;--sub:#999;--line:#333;--soft:#242424;--link:#8ab4d8;--acc:#86b79f}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN","Hiragino Sans",Meiryo,"Yu Gothic",sans-serif;font-size:16px;line-height:1.9;overflow-wrap:anywhere}
a{color:var(--link)}img{display:block;max-width:100%;height:auto}
.site{border-bottom:1px solid var(--line)}
.site .in{max-width:1080px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;gap:10px}
.site a{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--ink);font-weight:bold;font-size:1.05rem}
.site img{width:30px;height:30px;border-radius:50%}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px;display:grid;grid-template-columns:minmax(0,1fr);gap:40px}
@media (min-width:900px){.wrap{grid-template-columns:minmax(0,1fr) 280px}}
main{min-width:0;padding:24px 0 40px}
.intro{font-size:.92rem;color:var(--sub);margin:4px 0 20px}
.list a{display:flex;gap:14px;padding:16px 0;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.list img{width:120px;height:90px;object-fit:cover;object-position:top;border:1px solid var(--line);flex:none}
.list h2{font-size:1.02rem;line-height:1.6;margin:0 0 4px}
.list p{font-size:.84rem;color:var(--sub);line-height:1.7;margin:0}
.list small{font-size:.75rem;color:var(--sub)}
article h1{font-size:1.5rem;line-height:1.55;margin:4px 0 8px}
.meta{font-size:.8rem;color:var(--sub);margin:0 0 18px}
.pr-note{font-size:.78rem;color:var(--sub);background:var(--soft);padding:6px 10px;margin:0 0 20px}
article figure{margin:0 0 28px}
article figure img{border:1px solid var(--line);max-height:860px;width:auto}
article p{margin:0 0 1.4em}
.items{margin:32px 0 0;background:var(--soft);padding:14px 16px}
.items h2{font-size:.95rem;margin:0 0 6px}
.items li{margin:6px 0;font-size:.93rem}
.items ul{margin:0;padding-left:1.1em}
.related{margin-top:40px}
.related h2{font-size:1rem;border-bottom:2px solid var(--ink);padding-bottom:4px;margin:0}
aside{padding:24px 0 40px}
.box{border:1px solid var(--line);padding:16px;font-size:.85rem;line-height:1.8}
.box img{width:64px;height:64px;border-radius:50%;margin:0 0 8px}
.box b{display:block;font-size:.95rem;margin-bottom:4px}
.box p{margin:0 0 8px;color:var(--sub)}
footer{border-top:1px solid var(--line);font-size:.75rem;color:var(--sub)}
footer .in{max-width:1080px;margin:0 auto;padding:20px 16px 32px;line-height:1.8}
footer a{color:var(--sub)}"""

def page(title, desc, url, image, inner, kind="article"):
    t = html.escape(title); d = html.escape(desc)
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:site_name" content="6畳ラボ"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:type" content="{kind}"><meta property="og:url" content="{url}"><meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="img/icon.png"><link rel="stylesheet" href="style.css"></head>
<body><div class="site"><div class="in"><a href="./"><img src="img/icon.png" alt="">6畳ラボ</a></div></div>
<div class="wrap">{inner}
<aside><div class="box"><img src="img/icon.png" alt=""><b>6畳ラボ</b><p>6畳・ワンルームの賃貸の部屋づくりを、寸法と図でまとめています。ラグやカーテン、冬の寝具など、買う前に測っておきたいところが中心です。</p><p>紹介している商品は<a href="{ROOM}">楽天ROOM</a>にもまとめています。</p></div></aside></div>
<footer><div class="in">当サイトは楽天アフィリエイトに参加しています。【PR】の付いたリンクから商品が購入されると、当サイトに紹介料が入ることがあります。価格や在庫はリンク先でご確認ください。<br>© 6畳ラボ</div></footer>
</body></html>"""

def row(a):
    return (f'<a href="{a["slug"]}.html"><img src="img/{a["slug"]}-thumb.jpg" alt="" loading="lazy" width="120" height="90">'
            f'<div><h2>{html.escape(a["title"])}</h2><p>{html.escape(a["lede"])}</p><small>{html.escape(a["tag"])}</small></div></a>')

urls = []
date = f"{TODAY.year}年{TODAY.month}月{TODAY.day}日"
for i, a in enumerate(articles):
    save_images(a["pin"], a["slug"])
    url = BASE + a["slug"] + ".html"; urls.append(url)
    body = f"<p>{html.escape(a['lede'])}</p>" + "".join(f"<h2>{html.escape(x[1])}</h2>" if isinstance(x, tuple) else f"<p>{html.escape(x)}</p>" for x in a["body"])
    items = "".join(f'<li>【PR】<a href="{u}" rel="sponsored noopener" target="_blank">{html.escape(s)}</a>(楽天市場)</li>' for s, u in a["pr"])
    others = [b for b in articles if b is not a]
    others = (others[i:] + others[:i])[:3]
    inner = f"""<main><article>
<h1>{html.escape(a["title"])}</h1>
<p class="meta">{date} ・ {html.escape(a["tag"])}</p>
<p class="pr-note">この記事には楽天アフィリエイトのリンクが含まれています。</p>
<figure><img src="img/{a["slug"]}.jpg" alt="{html.escape(a["title"])}" width="900" height="1350"></figure>
{body}
<div class="items"><h2>紹介した商品</h2><ul>{items}</ul></div>
</article>
<section class="related"><h2>ほかの記事</h2><div class="list">{"".join(row(b) for b in others)}</div></section></main>"""
    with open(os.path.join(OUT, a["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(page(a["title"] + " - 6畳ラボ", a["desc"], url, BASE + "img/" + a["slug"] + ".jpg", inner))

index_inner = f"""<main><p class="intro">6畳・ワンルームの賃貸の部屋づくりを、寸法と図でまとめています。</p>
<div class="list">{"".join(row(a) for a in articles)}</div></main>"""
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page("6畳ラボ - 6畳・ワンルームの賃貸の部屋づくり", "6畳・ワンルームの賃貸で暮らす人に向けて、ラグやカーテンの大きさ、冬の寝具、退去費用まで、買う前に知っておきたい寸法と置き方を図にしています。", BASE, BASE + "img/rug-size.jpg", index_inner, "website"))
with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS)
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"<url><loc>{u}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>\n" for u in [BASE] + urls) + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print(len(urls), "articles")
