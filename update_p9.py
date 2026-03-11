#!/usr/bin/env python3
"""Update p9.html with content from original website, translating Chinese to English."""

# New content for p9.html (middle section only)
new_content = '''<div id="newscontent">
	<div id="newsconttitle">
		<h1>Compressor Working Principle and Structure</h1>
		<p><span style="float:right;">Views: 1338</span><span>2023-07-24 00:00:00   Source: </span><a href="Compressor Network">Compressor Network</a></p>
	</div>
    <div class="clear"></div>
    	<div id="newcontent">
		<p>
	<img src="upload/Image/20240829/20240829151517_58089.jpg" width="520" height="520" alt="" />
</p>
<p>
	<img src="upload/Image/20240829/20240829151623_95729.jpg" width="520" height="520" alt="" />
</p>
<p>
	Public interest repost and link
</p>
<p>
	<a href="https://mp.weixin.qq.com/s?__biz=MjM5MzM4MzUzMg==&amp;mid=2649774788&amp;idx=1&amp;sn=5b5e20e52747abe157cd2fbc3ce08580&amp;chksm=be932fc789e4a6d1c3b182d58acd4f638188e72225b6d4040969a50e9ac23db9dca849400ea7&amp;mpshare=1&amp;scene=24&amp;srcid=0823ULsYSEQT8DLXh1QTMnrP&amp;sharer_sharetime=1692746345938&amp;sharer_shareid=d181d01fc04705b5c28fff080efa6714&amp;ascene=14&amp;devicetype=android-33&amp;version=2800293e&amp;nettype=WIFI&amp;abtest_cookie=AAACAA%3D%3D&amp;lang=zh_CN&amp;countrycode=CN&amp;exportkey=n_ChQIAhIQXnIeMLdRsK4b61bT25xP4xLvAQIE97dBBAEAAAAAALa%2BLb0Pd%2B4AAAAOpnltbLcz9gKNyK89dVj0W29cC88aLKwZUcRbembIptJ8ldAEhEdbSHxh%2FrKJr1MLjvz7RLFhUtSIvqqcNd9tzlKjYxEhRHWjLjCdmdLFm71UdRm9QMDaCn0vUb0RIA1MQZ79hyn5SZg8a1y3j%2FnDPl5dceMqRITphnJ0MDhZgwe%2B%2Fy70Io%2FvQCstGqoCskpDb321LfsvTSsLLgb2g8WY%2FkKMuWZzWuAgipofGe0eQFMUiw0QWCjefAmRnjp4BPJnnTQQIdDLLBE7lnRSRPVFg9FqMbGScWDM&amp;pass_ticket=picK9diSn8Vubl7DPStdd%2FBLB2g8Hj0uTRattgyMtS6HbeAW%2F4%2BvlSSDa2a%2FvCvm&amp;wx_header=3" target="_blank">WeChat Article Link</a> 
</p>	</div>
	<div class="endPageNum">
		<table align="center">
			<tr>
				<td>
								<div class="clear"></div>
				</td>
			</tr>
		</table>
	</div>
	<div id="articeBottom"><span>[Editor: <a href="#">YSJW</a>]</span><a href="#">(Top) Return to top</a></div>
</div>
<div style="border:1px dashed #999999"></div>
<div id="articleHeader">
	<h4>Next: <a href="p9.html">5th Compressor Industry Development Annual Conference</a></h4>
	</div>'''

# Read current p9.html
with open('/Users/lijiemuhong/.openclaw/workspace/scyyge-english/p9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the newscontent section
import re

# Find the start of newscontent
start_match = re.search(r'<div id="newscontent">', content)
if not start_match:
    print("Could not find newscontent start")
    exit(1)

# Find the end - look for articleHeader closing
end_match = re.search(r'</div>\s*<div style="border:1px dashed #999999"></div>\s*<div id="articleHeader">', content)
if not end_match:
    print("Could not find articleHeader")
    exit(1)

# Replace the content
start_pos = start_match.start()
end_pos = end_match.end()

new_full_content = content[:start_pos] + new_content + content[end_pos:]

# Also update the title in newsconttitle
new_full_content = re.sub(
    r'<title>[^<]+</title>',
    '<title>Compressor Working Principle - Industry News - Sichuan Yiyuan</title>',
    new_full_content
)

# Update keywords
new_full_content = re.sub(
    r'<meta name="keywords" content="[^"]*"',
    '<meta name="keywords" content="Compressor, Working Principle, Industry News - Sichuan Yiyuan, Natural Gas Compressor"',
    new_full_content
)

# Update description
new_full_content = re.sub(
    r'<meta name="description" content="[^"]*"',
    '<meta name="description" content="Compressor working principle and structure - Industry News - Sichuan Yiyuan"',
    new_full_content
)

# Update page label
new_full_content = re.sub(
    r'<label>行业新闻</label>',
    '<label>Industry News</label>',
    new_full_content
)

with open('/Users/lijiemuhong/.openclaw/workspace/scyyge-english/p9.html', 'w', encoding='utf-8') as f:
    f.write(new_full_content)

print("✅ p9.html updated with new content from original website!")
print("   - Title translated: Compressor Working Principle and Structure")
print("   - Content translated to English")
print("   - Images preserved")
print("   - Links preserved")
