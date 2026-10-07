# 6畳ラボのサイトを作る。pages の中身から HTML を書き出し、図を縮小して img/ に置く。
import os, html, datetime
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
PINS = os.path.join(os.path.dirname(ROOT), "pins")
BASE = "https://kame6493-del.github.io/6jo-lab/"
TODAY = datetime.date.today().isoformat()
ROOM = "https://room.rakuten.co.jp/room_1c124220fb/items"

os.makedirs(os.path.join(OUT, "img"), exist_ok=True)

def img(src, name):
    im = Image.open(os.path.join(PINS, src)).convert("RGB")
    im.thumbnail((800, 1200))
    im.save(os.path.join(OUT, "img", name), "JPEG", quality=84, optimize=True)
    return "img/" + name

# 本文は (種類, 中身) の並び。p=段落 h=小見出し ul=箇条書き(リスト) pr=PRリンク(文, URL)
pages = [
  dict(slug="rug-size", pin="pin_6jo_rug.png",
    title="6畳に合うラグの大きさは？ベッドあり・なしで変わる目安",
    desc="6畳の部屋に置くラグの大きさの目安。ベッドがある部屋は130×185cm、ベッドがない部屋は185×185cm。床を少し残すと部屋が広く見えます。",
    body=[
      ("p", "ラグを選ぶとき、色や素材より先に決めておきたいのが大きさです。大きさが決まれば、あとは色と毛足を比べるだけになります。"),
      ("h", "迷ったらこの2つ"),
      ("ul", ["ベッドを置いている6畳なら、130×185cm前後(約1.5畳)。ベッドの横の床に敷くのにちょうどいい大きさです。",
              "ベッドを置かない6畳なら、185×185cm前後(約2畳)。ローテーブルを置いて、座る場所ごと敷けます。"]),
      ("h", "床を全部隠さない"),
      ("p", "6畳の床をほとんど覆うような大きいラグにすると、かえって部屋が狭く見えます。ラグの周りに床が少し見えているくらいが、部屋の広さが伝わりやすいです。"),
      ("p", "測るときは、ベッドや机の脚がラグに乗るかどうかも見ておくと、置いてからのずれが減ります。"),
      ("h", "冬は洗えるかどうかも"),
      ("p", "一人暮らしの部屋はラグの上で過ごす時間が長く、汚れやすいです。洗濯機で洗えるか、ホットカーペットの上に敷けるかを先に条件に入れておくと、長く使えるものを選びやすくなります。"),
      ("pr", "図の大きさ(130×185cm・185×185cm)があり、洗えるラグ", "https://a.r10.to/hFh9P3"),
    ]),
  dict(slug="curtain-size", pin="pin_curtain.png",
    title="カーテンのサイズの測り方｜測るのは窓ではなくレール",
    desc="カーテンの幅はレールの長さ×1.05、丈は掃き出し窓ならランナーの下から床まで−1cm、腰窓なら窓枠の下+15〜20cm。冬の冷気を防ぐ測り方。",
    body=[
      ("p", "カーテンを買う前に測るのは、窓の大きさではなくカーテンレールです。窓だけ測って買うと、幅が足りずに端がすいたり、丈が短くて光がもれたりします。"),
      ("h", "幅"),
      ("p", "レールの両端にある固定ランナー(動かない輪)の間を測り、1.05倍にします。少しゆとりがあると、閉めたときに端がすきません。両開きにするなら、その半分の幅を2枚です。"),
      ("h", "丈"),
      ("ul", ["掃き出し窓は、ランナー(フックを掛ける輪)の下から床までを測って、1cm引きます。床に付くと裾が汚れやすく、短すぎると下から光がもれます。",
              "腰窓は、ランナーの下から窓枠の下までを測って、15〜20cm足します。窓枠より下まで隠れると、すき間風と光もれが減ります。"]),
      ("h", "冬は少し長めが安心"),
      ("p", "窓のガラスで冷えた空気は、下へ落ちてきます。丈が短いと、その冷気がカーテンの下から部屋に入りやすくなります。腰窓は少し長めにしておくと、足元の冷えがやわらぎます。"),
      ("pr", "丈は1cm単位・幅は5cm単位で頼める1級遮光カーテン(日本製・洗える)", "https://a.r10.to/hPsggJ"),
    ]),
  dict(slug="winter-futon", pin="pin_fuyu_futon.png",
    title="冬の布団、何を足すと暖かい？一人暮らしの寝具は下から",
    desc="冬の寝具を足す順番の目安。まず敷きパッドを冬用に、次に掛け布団と体の間に毛布、それでも寒ければ掛け布団を冬用に。床が冷える6畳の部屋向け。",
    body=[
      ("p", "冬に布団が寒いと、まず掛け布団を厚くしたくなります。でも寒さは、体の下から来ていることが多いです。"),
      ("h", "足す順番の目安"),
      ("ul", ["敷きパッドを冬用(起毛のもの)に替える",
              "掛け布団と体の間に毛布を1枚入れる",
              "それでも寒ければ、掛け布団を冬用にする"]),
      ("p", "敷き布団やマットレスは、床の冷たさを直接受けます。下を先に暖かくすると、同じ掛け布団でも寒さの感じ方が変わります。"),
      ("h", "床に寝ている人は特に"),
      ("p", "ベッドを置かずに布団やマットレスを床に敷いている6畳では、床からの冷えが強くなります。ラグを1枚敷くだけでも、冷たさがやわらぎます。"),
      ("pr", "冬用の敷きパッド(洗濯機で洗える・シングルから)", "https://a.r10.to/hgGfzM"),
      ("pr", "洗濯機で洗えて、シングルからある毛布", "https://a.r10.to/hFOvgm"),
    ]),
  dict(slug="moufu", pin="pin_moufu.png",
    title="毛布を選ぶ前に見る3つ｜サイズ・洗えるか・素材",
    desc="毛布を選ぶときに見るのは、洗濯機で洗えるか、サイズ(シングルは140×200cm前後)、素材の3つ。一人暮らしなら洗えるかどうかが一番大事。",
    body=[
      ("p", "毛布は種類が多く、どれも暖かそうに見えます。迷ったら、次の3つを順に見ていくと絞れます。"),
      ("h", "1. 洗濯機で洗えるか"),
      ("p", "一人暮らしでは、大きな寝具をクリーニングに出す手間が続きません。洗濯機で洗えるものを選んでおくと、汚れを気にせず使えます。洗濯表示で、桶のマークに×が付いていないかを見ておきます。"),
      ("h", "2. サイズ"),
      ("p", "シングルの毛布は140×200cm前後が多いです。ベッドの幅より少し大きいと、寝返りをしてもはみ出しにくくなります。"),
      ("h", "3. 素材"),
      ("p", "ふわっとした手触りのものは、ポリエステルのマイクロファイバー系が多いです。軽くて乾きやすいのも、一人暮らしには助かるところです。"),
      ("pr", "洗濯機で洗えて、シングル・セミダブル・ダブルがある毛布", "https://a.r10.to/hFOvgm"),
    ]),
  dict(slug="mattress", pin="pin_mattress.png",
    title="マットレスを床に直置きするなら｜気をつけるのは湿気",
    desc="6畳でベッドを置かずにマットレスを床に置くなら、気をつけるのは下にこもる湿気。すのこを挟む、三つ折りを朝たたんで立てる、の2つが手軽です。",
    body=[
      ("p", "6畳の部屋では、ベッドを置かずにマットレスや布団を床に敷く人も多いです。床が空くのはいいところですが、気をつけたいのが湿気です。"),
      ("h", "下に汗がたまりやすい"),
      ("p", "寝ている間の汗は下へ抜けにくく、床とマットレスの間にこもりやすいです。敷いたままにしておくと、乾く時間がありません。"),
      ("h", "手軽な対策は2つ"),
      ("ul", ["すのこを1枚挟む。すき間から空気が通って、湿気が抜けやすくなります。",
              "三つ折りのマットレスなら、朝たたんで立てておく。床が空いて、マットレスの下も乾きます。"]),
      ("p", "ベッドを置かない6畳なら、この2つの組み合わせが手軽です。"),
      ("pr", "三つ折りで、シングルは97×195cm・厚さ10cmと5cm、カバーを外して洗えるマットレス", "https://a.r10.to/hgCsYc"),
    ]),
  dict(slug="mado-reiki", pin="pin_mado_reiki.png",
    title="冬の窓際が寒い理由と、賃貸でもできる3つの対策",
    desc="冬に窓際が寒いのは、ガラスで冷えた空気が床へ落ちてくるから。カーテンを床まで、窓の下に断熱パネル、寝る場所を窓から離す。賃貸でもできる対策。",
    body=[
      ("p", "冬、窓の近くにいると足元がすうっと冷えます。これは、窓のガラスで冷やされた空気が重くなり、窓に沿って下へ落ち、床を伝って部屋に広がるからです。"),
      ("h", "賃貸でもできる3つ"),
      ("ul", ["カーテンを床まで届く長さにする。下のすき間から冷気が出にくくなります。",
              "窓の下に断熱パネルを立てる。置くだけのものや、はがせるものなら原状回復の心配が少ないです。",
              "寝る場所を窓から少し離す。冷気が流れてくる通り道をよけられます。"]),
      ("p", "6畳の部屋は窓とベッドが近くなりがちです。家具の配置を考えるときに、窓からの距離も入れておくと冬が楽になります。"),
      ("pr", "6畳の冬支度(毛布・布団・ラグ)をまとめた楽天ROOM", "https://room.rakuten.co.jp/room_1c124220fb/collection/1800012748397273"),
    ]),
  dict(slug="taikyo", pin="pin_taikyo.png",
    title="退去費用、どこまで自分の負担？国交省ガイドラインの分け方",
    desc="国交省の原状回復ガイドラインでは、家具の跡や画びょうの穴、日焼けはふつうに暮らしてできたもの。タバコのヤニやネジ穴、放置したカビは借りた人の負担になりやすい。",
    body=[
      ("p", "賃貸を出るときの退去費用。どこまでが自分の負担なのかは、国土交通省の「原状回復をめぐるトラブルとガイドライン」がひとつの目安になります。"),
      ("h", "ふつうに暮らしてできたもの"),
      ("p", "家具を置いていた床のへこみ、画びょうやピンの穴、日焼けによる壁紙の色あせなどは、ふつうに暮らしていてできるものとして扱われています。"),
      ("h", "借りた人の負担になりやすいもの"),
      ("p", "タバコのヤニや臭い、壁に開けたネジ穴、手入れをせずに広がったカビなどは、借りた人の負担になりやすいとされています。"),
      ("h", "迷ったら、穴を残しにくい物を"),
      ("p", "棚や収納を壁に付けるなら、ネジではなくピンで留めるものや、突っ張り式のものを選んでおくと安心です。契約書に特約が書かれていることもあるので、先に確かめておきます。"),
      ("p", "入居した日に、床や壁の傷を日付が残る形で写真に撮っておくと、退去のときに説明しやすくなります。"),
      ("pr", "ピンや突っ張りで付けられる、壁に穴を残しにくい収納をまとめた楽天ROOM", "https://room.rakuten.co.jp/room_1c124220fb/collection/1800012748348292"),
    ]),
]

CSS = """:root{--bg:#faf7f2;--ink:#2d2d34;--sub:#6e6e78;--acc:#2f7d64;--card:#fff;--line:#e6dfd4}
@media (prefers-color-scheme:dark){:root{--bg:#1d1d20;--ink:#ecebe8;--sub:#a9a8b0;--acc:#6cc4a4;--card:#26262a;--line:#3a3a40}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"BIZ UDPGothic","Hiragino Sans","Noto Sans JP",sans-serif;line-height:1.85;font-size:17px}
.wrap{max-width:720px;margin:0 auto;padding:24px 16px 64px}header a{color:var(--ink);text-decoration:none;font-weight:700}
h1{font-size:1.55rem;line-height:1.5;margin:28px 0 8px}h2{font-size:1.15rem;margin:32px 0 6px;border-left:4px solid var(--acc);padding-left:10px}
.pr-note{font-size:.82rem;color:var(--sub);border:1px solid var(--line);border-radius:8px;padding:6px 10px;margin:12px 0}
figure{margin:20px 0}figure img{width:100%;height:auto;border-radius:10px;border:1px solid var(--line)}
.pr{display:block;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:14px 0;color:var(--ink);text-decoration:none}
.pr b{color:var(--acc)}.pr span{display:block;font-size:.85rem;color:var(--sub)}
ul{padding-left:1.2em}li{margin:6px 0}.list a{display:block;padding:14px 0;border-bottom:1px solid var(--line);color:var(--ink);text-decoration:none}
.list small{display:block;color:var(--sub)}footer{margin-top:48px;font-size:.85rem;color:var(--sub)}footer a{color:var(--sub)}"""

def head(title, desc, url, image):
    t = html.escape(title); d = html.escape(desc)
    return f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:type" content="article"><meta property="og:url" content="{url}"><meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="style.css"></head><body><div class="wrap">
<header><a href="./">6畳ラボ｜賃貸の部屋づくり</a></header>"""

FOOT = f"""<footer><p>6畳ラボは、6畳・ワンルームの賃貸で暮らす人向けに、寸法と置き方を図でまとめています。商品の紹介は<a href="{ROOM}">楽天ROOM</a>にもあります。</p>
<p>このサイトは楽天アフィリエイトに参加しています。【PR】と書いたリンクから商品が購入されると、紹介料を受け取ることがあります。価格や在庫はリンク先でご確認ください。</p></footer></div></body></html>"""

def render(p):
    url = BASE + p["slug"] + ".html"
    im = img(p["pin"], p["slug"] + ".jpg")
    out = [head(p["title"], p["desc"], url, BASE + im), f"<h1>{html.escape(p['title'])}</h1>",
           '<p class="pr-note">このページには楽天アフィリエイトのリンク(【PR】)が含まれています。</p>',
           f'<figure><img src="{im}" alt="{html.escape(p["title"])}の図" width="800" height="1200" loading="eager"></figure>']
    for item in p["body"]:
        kind, v = item[0], (item[1] if len(item) == 2 else item[1:])
        if kind == "p": out.append(f"<p>{html.escape(v)}</p>")
        elif kind == "h": out.append(f"<h2>{html.escape(v)}</h2>")
        elif kind == "ul": out.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in v) + "</ul>")
        elif kind == "pr":
            text, link = v
            out.append(f'<a class="pr" href="{link}" rel="sponsored noopener" target="_blank"><b>【PR】</b>{html.escape(text)}<span>楽天で見る →</span></a>')
    others = [q for q in pages if q is not p][:3]
    out.append("<h2>ほかの図</h2><div class=\"list\">" + "".join(f'<a href="{q["slug"]}.html">{html.escape(q["title"])}</a>' for q in others) + "</div>")
    out.append(FOOT)
    with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return url

urls = [render(p) for p in pages]
idx = [head("6畳ラボ｜6畳・ワンルームの賃貸の部屋づくり", "6畳・ワンルームの賃貸で暮らす人向けに、ラグやカーテンの大きさ、冬の寝具、退去費用まで、寸法と置き方を図でまとめています。", BASE, BASE + "img/rug-size.jpg"),
       "<h1>6畳・ワンルームの部屋づくりを、図で</h1>",
       "<p>6畳の部屋は、物を1つ置くだけで広さが変わります。ここでは、買う前に知っておきたい寸法と置き方を、自分で描いた図でまとめています。</p>",
       '<div class="list">' + "".join(f'<a href="{p["slug"]}.html">{html.escape(p["title"])}<small>{html.escape(p["desc"][:60])}…</small></a>' for p in pages) + "</div>", FOOT]
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write("\n".join(idx))
with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS)
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in [BASE] + urls) + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print(len(urls), "pages")
