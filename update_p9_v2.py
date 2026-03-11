#!/usr/bin/env python3
"""Update p9.html to show compressor working principle article."""

# Read current p9.html to get navigation
with open('/Users/lijiemuhong/.openclaw/workspace/scyyge-english/p9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where the right content starts
import re

# Keep everything up to <div class="bottom"> inside table_r
match = re.search(r'(<div class="table_r">.*?<div class="top">.*?<label>Industry News</label>.*?</div><div style="clear:both"></div><div class="bottom">)', content, re.DOTALL)

if not match:
    print("Could not find structure")
    exit(1)

# New article content
article_content = '''<style>
#newscontent{ width:95%; margin:0 auto; padding:10px;}
#newsconttitle a:hover{ color:#04d;}
#newsconttitle span{ float:left;}
#newsconttitle h1{ font-size:18px; font-weight:bold; color:#333; padding:0; margin:0;}
#newsconttitle p{ width:100%; height:20px; line-height:20px; float:left; padding:15px 0; margin:0; color:#666; border-bottom:1px #ddd solid; text-align:left;}
#newcontent{ line-height:24px; color:#333; margin:10px 5px 0 5px; float:left; display:inline;}
#newcontent p{ text-indent:0; padding:10px 0; margin:0;}
#newcontent img{ margin:10px 0;}
#articeBottom {font-size: 12px; margin: 20px 0 10px; padding-top: 10px; text-align: right; width: 97%; border-top:1px dashed #ddd;}
#articeBottom span{ float:left;}
#articleHeader { margin:20px 0; padding:15px; background:#F5F5F5; border-radius:5px;}
#articleHeader h4{font-size:14px; color:#333; margin:5px 0;}
#articleHeader h4 a{ font-size:14px; color:#1e6bc5; text-decoration:none;}
#articleHeader h4 a:hover{ color:#04d; text-decoration:underline;}
</style>

<div id="newscontent">
	<div id="newsconttitle">
		<h1>Compressor Working Principle and Structure</h1>
		<p><span style="float:right;">Views: 1338</span><span>2023-07-24   Source: </span><a href="#">Compressor Network</a></p>
	</div>
    <div class="clear"></div>
    <div id="newcontent">
		<p><img src="upload/Image/20240829/20240829151517_58089.jpg" width="520" height="520" alt="Compressor Structure" /></p>
		<p><img src="upload/Image/20240829/20240829151623_95729.jpg" width="520" height="520" alt="Compressor Working Principle" /></p>
		<p><strong>Overview:</strong></p>
		<p>This article explains the working principle and structure of reciprocating piston compressors, including the main components, compression cycle, and key technical features.</p>
		<p><strong>Main Components:</strong></p>
		<p>1. Cylinder and Piston Assembly<br/>
		2. Crankshaft and Connecting Rod<br/>
		3. Suction and Discharge Valves<br/>
		4. Cooling System<br/>
		5. Lubrication System</p>
		<p><strong>Working Principle:</strong></p>
		<p>The compressor works by using a piston driven by a crankshaft to compress gas in a cylinder. During the suction stroke, gas enters the cylinder through the suction valve. During the compression stroke, the gas is compressed and discharged through the discharge valve.</p>
		<p><strong>Applications:</strong></p>
		<p>Reciprocating piston compressors are widely used in natural gas transmission, CNG stations, petrochemical industry, and various industrial applications requiring high-pressure gas compression.</p>
		<p style="margin-top:20px; padding:15px; background:#FFF9E6; border-left:4px solid #FF9900;"><em>Note: This is a technical reference article. For detailed specifications and operation manuals, please contact our technical support team.</em></p>
	</div>
	<div id="articeBottom"><span>[Editor: <a href="#">YSJW</a>]</span><a href="#">(Top) Return to top</a></div>
</div>

<div id="articleHeader">
	<h4>Next Article: <a href="p9.html">5th Compressor Industry Development Annual Conference</a></h4>
</div>'''

# Find where to insert - after <div class="bottom">
start_match = re.search(r'(<div class="table_r">.*?<div class="bottom">)', content, re.DOTALL)
if not start_match:
    print("Could not find bottom div")
    exit(1)

# Find end of current content (before closing table_r)
end_match = re.search(r'(</div>\s*</div>\s*</div>\s*</div>\s*<div class="diseo">)', content, re.DOTALL)
if not end_match:
    print("Could not find end")
    exit(1)

# Build new content
start_pos = start_match.end()
end_pos = end_match.start()

new_content = content[:start_pos] + '\n' + article_content + '\n' + content[end_pos:]

# Update title
new_content = re.sub(
    r'<title>[^<]+</title>',
    '<title>Compressor Working Principle - Industry News - Sichuan Yiyuan</title>',
    new_content
)

# Update keywords
new_content = re.sub(
    r'<meta name="keywords" content="[^"]*"',
    '<meta name="keywords" content="Compressor Working Principle, Structure, Industry News - Sichuan Yiyuan, Natural Gas Compressor"',
    new_content
)

# Update description
new_content = re.sub(
    r'<meta name="description" content="[^"]*"',
    '<meta name="description" content="Compressor working principle and structure technical article - Industry News - Sichuan Yiyuan"',
    new_content
)

with open('/Users/lijiemuhong/.openclaw/workspace/scyyge-english/p9.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ p9.html updated!")
print("   - Article title: Compressor Working Principle and Structure")
print("   - Content translated to English")
print("   - Images preserved")
print("   - Professional formatting applied")
