 #-*- coding:utf-8 -*- python 3.6.2
import http.cookiejar
import urllib.request
import re

import os
from urllib.request import urlretrieve
from PIL import Image
import pytesseract

from bs4 import BeautifulSoup
html_doc="""

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>中路10分钟到newmarket shopping mall - 租房中心 -  新西兰天维网社区 -  Powered by Discuz!</title>
    <link href="http://bbs.skykiwi.com/forum.php?mod=viewthread&tid=3896975" rel="canonical" /><meta name="google-site-verification" content="s4kD2-70IFXkxDXROz3MwuA_MGHpQZzssTXTAgq6LSs" />
    <meta name="keywords" content="中路10分钟到newmarket shopping mall" />
    <meta name="description" content=" 中路10分钟到newmarket shopping mall ,新西兰天维网社区" />
    <meta name="generator" content="Discuz! X2" />
    <meta name="author" content="Discuz! Team and Comsenz UI Team" />
    <meta name="copyright" content="2001-2011 Comsenz Inc." />
    <meta name="MSSmartTagsPreventParsing" content="True" />
    <meta http-equiv="MSThemeCompatible" content="Yes" />
    <!-- <base href="http://bbs.skykiwi.com/" /> --><link rel="stylesheet" type="text/css" href="data/cache/style_1_common.css?anl" /><link rel="stylesheet" type="text/css" href="data/cache/style_1_forum_viewthread.css?anl" /><script type="text/javascript">var STYLEID = '1', STATICURL = 'static/', IMGDIR = 'static/image/common', VERHASH = 'anl', charset = 'utf-8', discuz_uid = '0', cookiepre = 'qqBC_2132_', cookiedomain = '', cookiepath = '/', showusercard = '1', attackevasive = '0', disallowfloat = 'newthread', creditnotice = '1|热情|,4|人气|', defaultstyle = '', REPORTURL = 'aHR0cDovL2Jicy5za3lraXdpLmNvbS9mb3J1bS5waHA/bW9kPXZpZXd0aHJlYWQmdGlkPTM4OTY5NzUmZXh0cmE9cGFnZSUzRDElMjZmaWx0ZXIlM0Rzb3J0aWQlMjZzb3J0aWQlM0QyODclMjZzb3J0aWQlM0QyODc=', SITEURL = 'http://bbs.skykiwi.com/', JSPATH = 'static/js/';</script>
    <script src="static/js/common.js?anl" type="text/javascript"></script><meta name="application-name" content="新西兰天维网社区" />
    <meta name="msapplication-tooltip" content="新西兰天维网社区" />
    <meta name="msapplication-task" content="name=论坛;action-uri=http://bbs.skykiwi.com/forum.php;icon-uri=http://bbs.skykiwi.com/static/image/common/bbs.ico" />
    <meta name="msapplication-task" content="name=家园;action-uri=http://bbs.skykiwi.com/home.php;icon-uri=http://bbs.skykiwi.com/static/image/common/home.ico" /><link rel="archives" title="新西兰天维网社区" href="http://bbs.skykiwi.com/archiver/" />
    <script src="static/js/forum.js?anl" type="text/javascript"></script>
    <!--通行证登陆登出接口 开始-->
    <script type="text/javascript">
    (function(d,b){d.PAPAPA=function(c,a,e,b){c=c||"";a=a||{};e=e||"";b=b||function(){};var f=function(a){var b=[],c;for(c in a)a.hasOwnProperty(c)&&b.push(c);return b};if("object"==typeof a){for(var g="",f=f(a),h=0;h<f.length;h++)g+=encodeURIComponent(f[h])+"="+encodeURIComponent(a[f[h]]),h!=f.length-1&&(g+="&");c+="?"+g}else"function"==typeof a&&(b=e=a);"function"==typeof e&&(b=e,e="jsoncallback");Date.now||(Date.now=function(){return(new Date).getTime()});a=Date.now();var k="jsonp"+Math.round(a+1000001*Math.random());d[k]=function(a){b(a);delete d[k]};c=-1===c.indexOf("?")?c+"?":c+"&";a=document.createElement("script");a.setAttribute("src",c+e+"="+k);document.getElementsByTagName("head")[0].appendChild(a)}})(window);function altRd(msg){alert(msg);alert("点击确定后将转跳至天维通行证首页，请在天维通行证的引导下正常登录。");window.location.href="https://passport.skykiwi.com"};function lin(d,b,c,a,e){b=document.getElementById(b).checked?"1":"0";c=document.getElementById(c).value;a=document.getElementById(a).value;PAPAPA(d,{isRemember:b,username:c,password:a,source:"webforum",backurl:e?e:window.location.href},function(a){"1"==a.signal?window.location.href=a.data.backurl:altRd(a.msg)})}function lout(d){PAPAPA(d,{source:"webforum",backurl:window.location.href},function(b){"1"==b.signal?b.referer?window.location.href=b.referer:window.location.reload():alert(b.msg)})};
    </script>
    <!--通行证登陆登出接口 结束-->

    <!-- 数据统计 mixpanel 开始-->
    <!-- start Mixpanel --><script type="text/javascript">(function(e,a){if(!a.__SV){var b=window;try{var c,l,i,j=b.location,g=j.hash;c=function(a,b){return(l=a.match(RegExp(b+"=([^&]*)")))?l[1]:null};g&&c(g,"state")&&(i=JSON.parse(decodeURIComponent(c(g,"state"))),"mpeditor"===i.action&&(b.sessionStorage.setItem("_mpcehash",g),history.replaceState(i.desiredHash||"",e.title,j.pathname+j.search)))}catch(m){}var k,h;window.mixpanel=a;a._i=[];a.init=function(b,c,f){function e(b,a){var c=a.split(".");2==c.length&&(b=b[c[0]],a=c[1]);b[a]=function(){b.push([a].concat(Array.prototype.slice.call(arguments,
    0)))}}var d=a;"undefined"!==typeof f?d=a[f]=[]:f="mixpanel";d.people=d.people||[];d.toString=function(b){var a="mixpanel";"mixpanel"!==f&&(a+="."+f);b||(a+=" (stub)");return a};d.people.toString=function(){return d.toString(1)+".people (stub)"};k="disable time_event track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config reset people.set people.set_once people.increment people.append people.union people.track_charge people.clear_charges people.delete_user".split(" ");
    for(h=0;h<k.length;h++)e(d,k[h]);a._i.push([b,c,f])};a.__SV=1.2;b=e.createElement("script");b.type="text/javascript";b.async=!0;b.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===e.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";c=e.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c)}})(document,window.mixpanel||[]);
    mixpanel.init("57f02aa5b3e7c7dddf87d35df19982ca");</script><!-- end Mixpanel -->
    <!--数据统计 mixpanel 结束-->

    </head>

    <body id="nv_forum" class="pg_viewthread" onkeydown="if(event.keyCode==27) return false;">
    <!-- 临时提醒全站版头 开始-->
    <!--
    <div style="background: #d62c3c; height: 30px; font-size: 15px; line-height: 30px; text-align: center; font-weight: bolder;"><a href="http://bbs.skykiwi.com/forum.php?mod=viewthread&amp;tid=2926683" style="color: #FFF; letter-spacing: 1px;">请注意防诈骗！关于论坛出现的盗号诈骗的温馨提醒</a></div>
    -->
    <!-- 临时提醒全站版头 结束-->
    <div id="append_parent"></div><div id="ajaxwaitid"></div>

    <div id="toptb" class="cl" style="padding: 5px 0; background: #F7F7F7; border-bottom: 1px solid #D6D6D6;">
    <div class="wp">
    <div class="z"></div>
    <div class="y">
    <a href="http://www.skykiwi.com" target="_blank" >天维首页</a><a href="http://news.skykiwi.com/" target="_blank" >新闻频道</a><a href="http://welly.skykiwi.com/" target="_blank" >天维惠灵顿</a><a href="http://mobile.skykiwi.com/" target="_blank"  style="font-weight: bold;color: red">天维生活</a><a href="http://www.wellcome.co.nz/" target="_blank"  style="font-weight: bold;color: green">纽惠康商城</a><a href="http://friends.skykiwi.com/" target="_blank" >天维伙伴</a><a href="http://imedu.skykiwi.com/" target="_blank" >留学移民</a><a href="http://money.skykiwi.com/" target="_blank"  style="font-weight: bold;color: blue">房产财经</a><a href="http://mobile.skykiwi.com/shop/index" target="_blank" >橙页搜索</a><a href="javascript:;" onclick="widthauto(this)">切换到宽版</a>
    </div>
    </div>
    </div>


    <div id="qmenu_menu" class="p_pop blk" style="display: none;">
    <div class="ptm pbw hm">
    请 <a href="https://passport.skykiwi.com/v1/login/bbslogon.do"><strong>登录</strong></a> 后使用快捷导航<br />没有帐号？<a href="https://passport.skykiwi.com/v1/login/bbslogon.do">注册</a>
    </div>
    </div>
    <div id="hd">
    <div class="wp">
    <div class="hdc cl"><h2><a href="./" title="新西兰天维网社区"><img src="http://img.skykiwi.com/logo/skykiwi.png" alt="新西兰天维网社区" border="0" /></a></h2>

    <script src="static/js/logging.js?anl" type="text/javascript"></script>
    <form method="post" autocomplete="off" id="lsform" action="member.php?mod=logging&amp;action=login&amp;loginsubmit=yes&amp;infloat=yes&amp;lssubmit=yes" onsubmit="return lsSubmit()">
    <div class="fastlg cl">
    <span id="return_ls" style="display:none"></span>
    <div class="y pns">
    <table cellspacing="0" cellpadding="0">
    <tr style="display:none;">
    <td><label for="ls_username">帐号</label></td>
    <td><input type="text" name="username" id="ls_username" class="px vm xg1"  value="UID/用户名/Email" onfocus="if(this.value == 'UID/用户名/Email'){this.value = '';this.className = 'px vm';}" onblur="if(this.value == ''){this.value = 'UID/用户名/Email';this.className = 'px vm xg1';}" tabindex="901" /></td>
    <td class="fastlg_l"><label for="ls_cookietime"><input type="checkbox" name="cookietime" id="ls_cookietime" class="pc" value="2592000" tabindex="903" />自动登录</label></td>
    <td>&nbsp;<a href="javascript:;" onclick="showWindow('login', 'member.php?mod=logging&action=login&viewlostpw=1')">找回密码</a></td>
    </tr>
    <tr>
    <td style="display:none;"><label for="ls_password">密码</label></td>
    <td style="display:none;"><input type="password" name="password" id="ls_password" class="px vm" autocomplete="off" tabindex="902" /></td>
    <td style="width:150px;display:inline-block;padding:10px 0;margin-right:10px;"><a href="http://passport.skykiwi.com" target="_blank"><img src="https://img.skykiwi.com/logo/passport.png" style="width:100%;"></a></td>
    <!-- <td class="fastlg_l" style="border:none;"><button type="submit" class="pn vm" tabindex="904" style="width:125px;height:31px;"><em>通行证登录/注册登录</em></button></td> -->
    <td><a href="https://passport.skykiwi.com/v1/login/bbslogon.do" style="background: #f7f7f7;display: inline-block;width: 100px;height: 30px;text-align: center;border: 1px solid #cacaca;line-height: 30px;border-radius: 5px;text-decoration: none;">登录</a></td>
    <td style="display:none;">&nbsp;<a href="member.php?mod=register2013" class="xi2 xw1">注册</a></td>
    </tr>
    </table>
    <input type="hidden" name="quickforward" value="yes" />
    <input type="hidden" name="handlekey" value="ls" />
    </div>
    </div>
    </form>
    </div>

    <div id="nv">
    <a href="javascript:;" id="qmenu" onmouseover="showMenu({'ctrlid':'qmenu','pos':'34!','ctrlclass':'a','duration':2});">快捷导航</a>
    <ul><li class="a" id="mn_forum" ><a href="forum.php" hidefocus="true" title="BBS"  >论坛<span>BBS</span></a></li><li id="mn_N647b" ><a href="http://bbs.skykiwi.com/forum.php?mod=announcement" hidefocus="true" title="Group"  >公告<span>Group</span></a></li><li id="mn_home" ><a href="home.php" hidefocus="true" title="Space"  >家园<span>Space</span></a></li><li id="mn_Nb8f0" ><a href="http://bbs.skykiwi.com/home.php?mod=task" hidefocus="true"  >任务</a></li><li id="mn_N0a2c" ><a href="misc.php?mod=faq" hidefocus="true" title="Help"  >帮助<span>Help</span></a></li><li id="mn_N3ee5" ><a href="https://passport.skykiwi.com/v1/passport/faq.do" hidefocus="true"  >通行证常见问题</a></li></ul>
    </div>
    <div id="mu" class="cl">
    </div><div id="scbar" class="cl"><form id="scbar_form" method="post" autocomplete="off" onsubmit="searchFocus($('scbar_txt'))" action="search.php?searchsubmit=yes" target="_blank">
    <input type="hidden" name="mod" id="scbar_mod" value="search" />
    <input type="hidden" name="formhash" value="cec12cfe" />
    <input type="hidden" name="srchtype" value="title" />
    <input type="hidden" name="srhfid" value="19" id="dzsearchforumid" />
    <input type="hidden" name="srhlocality" value="forum::viewthread" />
    <table cellspacing="0" cellpadding="0">
    <tr>
    <td class="scbar_icon_td"></td>
    <td class="scbar_txt_td"><input type="text" name="srchtxt" id="scbar_txt" value="请输入搜索内容" autocomplete="off" /></td>
    <td class="scbar_type_td"><a href="javascript:;" id="scbar_type" class="showmenu xg1 xs2" onclick="showMenu(this.id)" hidefocus="true">搜索</a></td>
    <td class="scbar_btn_td"><button type="submit" name="searchsubmit" id="scbar_btn" class="pn pnc" value="true"><strong class="xi2 xs2">搜索</strong></button></td>
    <td class="scbar_hot_td">
    <div id="scbar_hot">
    </div>
    </td>
    </tr>
    </table>
    </form>
    </div>
    <ul id="scbar_type_menu" class="p_pop" style="display: none;"><li><a href="javascript:;" rel="curforum" class="curtype">本版</a></li><li><a href="javascript:;" rel="user">用户</a></li></ul>
    <script type="text/javascript">
    initSearchmenu('scbar', '');
    </script>
    </div>
    </div>


    <div id="wp" class="wp"><script type="text/javascript">var fid = parseInt('19'), tid = parseInt('3896975');</script>

    <script src="static/js/forum_viewthread.js?anl" type="text/javascript"></script>
    <script type="text/javascript">zoomstatus = parseInt(1);var imagemaxwidth = '750';var aimgcount = new Array();</script>

    <style id="diy_style" type="text/css">#frameCFhY1F {  border:0px none !important;}#framefq8Iys {  border:0px !important;margin:0px !important;}#portal_block_279 {  border:#000000 0px none !important;margin-top:0px !important;margin-right:0px !important;margin-bottom:10px !important;margin-left:0px !important;}#portal_block_279 .dxb_bc {  margin:0px !important;}#frameHKHXTy {  border:0px !important;margin:0px !important;}#portal_block_301 {  border:0px !important;margin-top:10px !important;margin-right:0px !important;margin-bottom:0px !important;margin-left:0px !important;}#portal_block_301 .dxb_bc {  margin:0px !important;}</style>
    <!--[diy=diynavtop]--><div id="diynavtop" class="area"><div id="frameHKHXTy" class=" frame move-span cl frame-1"><div id="frameHKHXTy_left" class="column frame-1-c"><div id="frameHKHXTy_left_temp" class="move-span temp"></div><div id="portal_block_301" class="block move-span"><div id="portal_block_301_content" class="dxb_bc"><div class="portal_block_summary"><script type='text/javascript'><!--//<![CDATA[
    document.MAX_ct0 = unescape('INSERT_ENCODED_CLICKURL_HERE');

    var m3_u = (location.protocol=='https:'?'https://interactives.skykiwi.com/www/delivery/ajs.php':'http://interactives.skykiwi.com/www/delivery/ajs.php');
    var m3_r = Math.floor(Math.random()*99999999999);
    if (!document.MAX_used) document.MAX_used = ',';
    document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
    document.write ("?zoneid=61");
    document.write ('&amp;cb=' + m3_r);
    if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
    document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
    document.write ("&amp;loc=" + escape(window.location));
    if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
    if (document.context) document.write ("&context=" + escape(document.context));
    if ((typeof(document.MAX_ct0) != 'undefined') && (document.MAX_ct0.substring(0,4) == 'http')) {
        document.write ("&amp;ct0=" + escape(document.MAX_ct0));
    }
    if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
    document.write ("'></scr"+"ipt>");
    //]]>--></script><noscript><a href='http://interactives.skykiwi.com/www/delivery/ck.php?n=adf873fd&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://interactives.skykiwi.com/www/delivery/avw.php?zoneid=61&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=adf873fd&amp;ct0=INSERT_ENCODED_CLICKURL_HERE' border='0' alt='' /></a></noscript></div></div></div></div></div></div><!--[/diy]-->
    <div id="pt" class="bm cl">
    <div class="z">
    <a href="./" class="nvhm" title="首页">新西兰天维网社区</a> <em>&rsaquo;</em> <a href="forum.php">论坛</a> <em>&rsaquo;</em> <a href="forum.php?gid=269">天维交易</a> <em>&rsaquo;</em> <a href="forum.php?mod=forumdisplay&fid=19&page=1&filter=sortid&sortid=287">租房中心</a> <em>&rsaquo;</em> <a href="forum.php?mod=viewthread&amp;tid=3896975">中路10分钟到newmarket shopping mall</a>
    </div>
    </div>

    <style id="diy_style" type="text/css">#frameCFhY1F {  border:0px none !important;}#framefq8Iys {  border:0px !important;margin:0px !important;}#portal_block_279 {  border:#000000 0px none !important;margin-top:0px !important;margin-right:0px !important;margin-bottom:10px !important;margin-left:0px !important;}#portal_block_279 .dxb_bc {  margin:0px !important;}#frameHKHXTy {  border:0px !important;margin:0px !important;}#portal_block_301 {  border:0px !important;margin-top:10px !important;margin-right:0px !important;margin-bottom:0px !important;margin-left:0px !important;}#portal_block_301 .dxb_bc {  margin:0px !important;}</style>
    <div class="wp">
    <!--[diy=diy1]--><div id="diy1" class="area"></div><!--[/diy]-->
    </div>

    <div id="ct" class="wp cl">
    <div id="pgt" class="pgs mbm cl ">
    <div class="pgt"><div class="pg"><strong>1</strong><a href="forum.php?mod=viewthread&tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;page=2">2</a><a href="forum.php?mod=viewthread&tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;page=2" class="nxt">下一页</a></div></div>
    <span class="y pgb" id="visitedforums" onmouseover="$('visitedforums').id = 'visitedforumstmp';this.id = 'visitedforums';showMenu({'ctrlid':this.id,'pos':'34'})"><a href="forum.php?mod=forumdisplay&fid=19&page=1&filter=sortid&sortid=287">返回列表</a></span>
    <a id="newspecial" onmouseover="$('newspecial').id = 'newspecialtmp';this.id = 'newspecial';showMenu({'ctrlid':this.id})" onclick="location.href='forum.php?mod=post&action=newthread&fid=19';return false;" href="javascript:;" title="发新帖"><img src="static/image/common/pn_post.png" alt="发新帖" /></a></div>



    <div id="postlist" class="pl bm">
    <table cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls ptm pbm">
    <div class="hm">
    <span class="xg1">查看:</span> <span class="xi1">502</span><span class="pipe">|</span><span class="xg1">回复:</span> <span class="xi1">40</span>
    </div>
    </td>
    <td class="plc ptm pbn">
    <div class="y">
    <a href="forum.php?mod=viewthread&amp;action=printable&amp;tid=3896975" title="打印" target="_blank"><img src="static/image/common/print.png" alt="打印" class="vm" /></a>
    <a href="forum.php?mod=redirect&amp;goto=nextoldset&amp;tid=3896975" title="上一主题"><img src="static/image/common/thread-prev.png" alt="上一主题" class="vm" /></a>
    <a href="forum.php?mod=redirect&amp;goto=nextnewset&amp;tid=3896975" title="下一主题"><img src="static/image/common/thread-next.png" alt="下一主题" class="vm" /></a>
    </div>
    <h1 class="ts">
    <a href="forum.php?mod=forumdisplay&amp;fid=19&amp;filter=typeid&amp;typeid=33">[市中心]</a>
    <a href="forum.php?mod=viewthread&amp;tid=3896975" id="thread_subject">中路10分钟到newmarket shopping mall</a>
    <span class="xw0 xs1 xg1">
    <a href="forum.php?mod=viewthread&amp;tid=3896975" onclick="return copyThreadUrl(this)" title="您的朋友访问此链接后，您将获得相应的积分奖励">[复制链接]</a>
    </span>
    </h1>
    </td>
    </tr>
    </table>


    <table cellspacing="0" cellpadding="0" class="ad"><tr><td class="pls"></td><td class="plc"></td></tr></table><div id="post_71042797"><table id="pid71042797" summary="pid71042797" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <a name="newpost"></a> <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71042797" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71042797_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71042797')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71042797" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71042797_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71042797" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71042797_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71042797" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71042797" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71042797&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <div id="fj" class="y">
    <label class="z">电梯直达</label>
    <input type="text" class="px p_fre z" size="2" onkeyup="$('fj_btn').href='forum.php?mod=redirect&ptid=3896975&authorid=0&postno='+this.value" onkeydown="if(event.keyCode==13) {window.location=$('fj_btn').href;return false;}" title="跳转到指定楼层" />
    <a href="javascript:;" id="fj_btn" class="z" title="跳转到指定楼层"><img src="static/image/common/fj_btn.png" alt="跳转到指定楼层" class="vm" /></a>
    </div>
    <strong>
    <a href="forum.php?mod=viewthread&tid=3896975" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71042797" onclick="setCopy(this.href, '帖子地址复制成功');return false;">楼主</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71042797" src="static/image/common/online_member.gif" />
    <em id="authorposton71042797">发表于 2020-4-4 16:27:02</em>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;ordertype=1">倒序浏览</a>
    <strong>
    <a href="forum.php?mod=viewthread&tid=3896975" id="qrcode71042797" onclick="qrcodeDisplay(this.href, 'qrcode71042797');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><style type="text/css">.pcb{margin-right:0}</style><div class="pcb">
    <style type="text/css">
        .table-margin {margin: 30px 0;}

        .td-title {color:#484848; font-size:13px; font-weight:bold; background-color:#e1e1e1; padding: 7px 14px 7px 0; }

        .td-content {font-size:13px; padding-left:14px; background-color:#f5f5f5; }

        .table-container { padding:30px 0; margin-bottom:30px; border-bottom:dashed 1px #cdcdcd; }
    </style>
    <div class="table-container">
        <table cellpadding="2" cellspacing="0" border="1"  bordercolor="#fff" height="30">
            <tr>
                <td class="td-title" width="85" align="right">类型:</td>
                <td class="td-content">房间单租 Room</td>
            </tr>
            <tr>
                <td class="td-title" width="85" align="right">每周租金:</td>
                <td class="td-content">240 NZD</td>
            </tr>
            <tr>
                <td class="td-title" width="85" align="right">微信:</td>
                <td class="td-content">wxid_yo20xhu7fxyt22</td>
            </tr>
            <tr>
                <td class="td-title" width="85" align="right">联系电话:</td>
                <td class="td-content"><image src="forum.php?mod=misc&action=protectsort&tid=3896975&sortvalue=izJFwXGri1qOwoJNv71LB1ZcdWjIKddM%2FOaNWmHFjx8%3D"></td>
            </tr>

        </table>
    </div><div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71042797">
    <i class="pstatus"> 本帖最后由 汤圆 于 2020-5-14 12:11 编辑 </i><font class="jammer">7 @/ A5 |, [&nbsp;&nbsp;e/ H' k</font><br />
    <br />
    <span style="display:none">8 f! W5 a( @0 d* a</span><font size="6">招租女生一位，与友善女房东同住，近newmarket商业中心，交通购物餐饮皆方便，非常适合city以及附近上学或者上班的女生居住，居住环境优雅安静。有意者请联系：021865168</font><br />
    <span style="display:none">7 s. b1 W6 \+ I. }</span><font class="jammer">0 T0 W- g2 v4 c</font><br />
    </td></tr></table>
    </div>
    <div id="comment_71042797" class="cm">
    </div>
    <div id="post_rate_div_71042797"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    <div id="p_btn" class="mtw mbm cl">
    <a href="home.php?mod=spacecp&amp;ac=share&amp;type=thread&amp;id=3896975" id="k_share" onclick="showWindow(this.id, this.href, 'get', 0);" onmouseover="this.title = $('sharenumber').innerHTML + ' 人分享'"><i><img src="static/image/common/oshr.png" alt="分享" />分享<span id="sharenumber">0</span></i></a>
    <a href="home.php?mod=spacecp&amp;ac=favorite&amp;type=thread&amp;id=3896975" id="k_favorite" onclick="showWindow(this.id, this.href, 'get', 0);" onmouseover="this.title = $('favoritenumber').innerHTML + ' 人收藏'"><i><img src="static/image/common/fav.gif" alt="收藏" />收藏<span id="favoritenumber">1</span></i></a>
    </div>
    <div class="a_pb"><!-- Sky Media Ltd Javascript Tag - Generated with Revive Adserver v4.1.4 -->
    <script type='text/javascript'><!--//<![CDATA[
    document.MAX_ct0 = unescape('INSERT_ENCODED_CLICKURL_HERE');

    var m3_u = (location.protocol=='https:'?'https://interactives.skykiwi.com/www/delivery/ajs.php':'http://interactives.skykiwi.com/www/delivery/ajs.php');
    var m3_r = Math.floor(Math.random()*99999999999);
    if (!document.MAX_used) document.MAX_used = ',';
    document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
    document.write ("?zoneid=74");
    document.write ('&amp;cb=' + m3_r);
    if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
    document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
    document.write ("&amp;loc=" + escape(window.location));
    if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
    if (document.context) document.write ("&context=" + escape(document.context));
    if ((typeof(document.MAX_ct0) != 'undefined') && (document.MAX_ct0.substring(0,4) == 'http')) {
        document.write ("&amp;ct0=" + escape(document.MAX_ct0));
    }
    if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
    document.write ("'><\/scr"+"ipt>");
    //]]>--></script><noscript><a href='http://interactives.skykiwi.com/www/delivery/ck.php?n=ac7247ae&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://interactives.skykiwi.com/www/delivery/avw.php?zoneid=74&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=ac7247ae&amp;ct0=INSERT_ENCODED_CLICKURL_HERE' border='0' alt='' /></a></noscript>

    </div></td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71042797', 'misc.php?mod=report&rtype=post&rid=71042797&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71083112"><table id="pid71083112" summary="pid71083112" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71083112" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71083112_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71083112')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71083112" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71083112_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71083112" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71083112_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71083112" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71083112" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71083112&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71083112" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71083112" onclick="setCopy(this.href, '帖子地址复制成功');return false;">沙发</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71083112" src="static/image/common/online_member.gif" />
    <em id="authorposton71083112">发表于 2020-4-12 21:22:22</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71083112" id="qrcode71083112" onclick="qrcodeDisplay(this.href, 'qrcode71083112');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71083112">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71083112" class="cm">
    </div>
    <div id="post_rate_div_71083112"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    <div class="a_pb"><!-- Sky Media Ltd Javascript Tag - Generated with Revive Adserver v4.1.4 -->
    <script type='text/javascript'><!--//<![CDATA[
    document.MAX_ct0 = unescape('INSERT_ENCODED_CLICKURL_HERE');

    var m3_u = (location.protocol=='https:'?'https://interactives.skykiwi.com/www/delivery/ajs.php':'http://interactives.skykiwi.com/www/delivery/ajs.php');
    var m3_r = Math.floor(Math.random()*99999999999);
    if (!document.MAX_used) document.MAX_used = ',';
    document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
    document.write ("?zoneid=75");
    document.write ('&amp;cb=' + m3_r);
    if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
    document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
    document.write ("&amp;loc=" + escape(window.location));
    if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
    if (document.context) document.write ("&context=" + escape(document.context));
    if ((typeof(document.MAX_ct0) != 'undefined') && (document.MAX_ct0.substring(0,4) == 'http')) {
        document.write ("&amp;ct0=" + escape(document.MAX_ct0));
    }
    if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
    document.write ("'><\/scr"+"ipt>");
    //]]>--></script><noscript><a href='http://interactives.skykiwi.com/www/delivery/ck.php?n=a2ccbd38&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://interactives.skykiwi.com/www/delivery/avw.php?zoneid=75&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=a2ccbd38&amp;ct0=INSERT_ENCODED_CLICKURL_HERE' border='0' alt='' /></a></noscript></div></td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71083112', 'misc.php?mod=report&rtype=post&rid=71083112&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71088941"><table id="pid71088941" summary="pid71088941" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71088941" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71088941_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71088941')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71088941" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71088941_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71088941" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71088941_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71088941" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71088941" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71088941&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71088941" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71088941" onclick="setCopy(this.href, '帖子地址复制成功');return false;">板凳</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71088941" src="static/image/common/online_member.gif" />
    <em id="authorposton71088941">发表于 2020-4-14 11:16:53</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71088941" id="qrcode71088941" onclick="qrcodeDisplay(this.href, 'qrcode71088941');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71088941">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71088941" class="cm">
    </div>
    <div id="post_rate_div_71088941"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71088941', 'misc.php?mod=report&rtype=post&rid=71088941&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71102923"><table id="pid71102923" summary="pid71102923" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71102923" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71102923_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71102923')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71102923" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71102923_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71102923" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71102923_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71102923" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71102923" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71102923&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71102923" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71102923" onclick="setCopy(this.href, '帖子地址复制成功');return false;">地板</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71102923" src="static/image/common/online_member.gif" />
    <em id="authorposton71102923">发表于 2020-4-17 11:02:24</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71102923" id="qrcode71102923" onclick="qrcodeDisplay(this.href, 'qrcode71102923');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71102923">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71102923" class="cm">
    </div>
    <div id="post_rate_div_71102923"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71102923', 'misc.php?mod=report&rtype=post&rid=71102923&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71114725"><table id="pid71114725" summary="pid71114725" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71114725" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71114725_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71114725')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71114725" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71114725_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71114725" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71114725_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71114725" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71114725" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71114725&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71114725" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71114725" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>5</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71114725" src="static/image/common/online_member.gif" />
    <em id="authorposton71114725">发表于 2020-4-19 15:44:08</em>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71114725" id="qrcode71114725" onclick="qrcodeDisplay(this.href, 'qrcode71114725');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71114725">
    <br />
    <span style="display:none">- g* ~* C4 e4 u</span>好房出租！</td></tr></table>
    </div>
    <div id="comment_71114725" class="cm">
    </div>
    <div id="post_rate_div_71114725"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71114725', 'misc.php?mod=report&rtype=post&rid=71114725&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71126987"><table id="pid71126987" summary="pid71126987" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71126987" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71126987_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71126987')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71126987" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71126987_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71126987" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71126987_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71126987" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71126987" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71126987&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71126987" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71126987" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>6</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71126987" src="static/image/common/online_member.gif" />
    <em id="authorposton71126987">发表于 2020-4-21 16:09:36</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71126987" id="qrcode71126987" onclick="qrcodeDisplay(this.href, 'qrcode71126987');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71126987">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71126987" class="cm">
    </div>
    <div id="post_rate_div_71126987"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71126987', 'misc.php?mod=report&rtype=post&rid=71126987&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71147483"><table id="pid71147483" summary="pid71147483" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71147483" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71147483_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71147483')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71147483" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71147483_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71147483" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71147483_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71147483" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71147483" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71147483&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71147483" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71147483" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>7</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71147483" src="static/image/common/online_member.gif" />
    <em id="authorposton71147483">发表于 2020-4-24 19:12:58</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71147483" id="qrcode71147483" onclick="qrcodeDisplay(this.href, 'qrcode71147483');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71147483">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71147483" class="cm">
    </div>
    <div id="post_rate_div_71147483"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71147483', 'misc.php?mod=report&rtype=post&rid=71147483&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71151403"><table id="pid71151403" summary="pid71151403" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71151403" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71151403_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71151403')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71151403" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71151403_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71151403" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71151403_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71151403" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71151403" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71151403&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71151403" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71151403" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>8</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71151403" src="static/image/common/online_member.gif" />
    <em id="authorposton71151403">发表于 2020-4-25 12:14:26</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71151403" id="qrcode71151403" onclick="qrcodeDisplay(this.href, 'qrcode71151403');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71151403">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71151403" class="cm">
    </div>
    <div id="post_rate_div_71151403"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71151403', 'misc.php?mod=report&rtype=post&rid=71151403&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71155099"><table id="pid71155099" summary="pid71155099" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71155099" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71155099_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71155099')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71155099" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71155099_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71155099" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71155099_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71155099" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71155099" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71155099&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71155099" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71155099" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>9</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71155099" src="static/image/common/online_member.gif" />
    <em id="authorposton71155099">发表于 2020-4-25 20:41:26</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71155099" id="qrcode71155099" onclick="qrcodeDisplay(this.href, 'qrcode71155099');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71155099">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71155099" class="cm">
    </div>
    <div id="post_rate_div_71155099"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71155099', 'misc.php?mod=report&rtype=post&rid=71155099&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71160022"><table id="pid71160022" summary="pid71160022" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71160022" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71160022_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71160022')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71160022" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71160022_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71160022" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71160022_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71160022" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71160022" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71160022&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71160022" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71160022" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>10</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71160022" src="static/image/common/online_member.gif" />
    <em id="authorposton71160022">发表于 2020-4-26 14:38:06</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71160022" id="qrcode71160022" onclick="qrcodeDisplay(this.href, 'qrcode71160022');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71160022">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71160022" class="cm">
    </div>
    <div id="post_rate_div_71160022"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71160022', 'misc.php?mod=report&rtype=post&rid=71160022&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71168971"><table id="pid71168971" summary="pid71168971" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71168971" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71168971_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71168971')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71168971" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71168971_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71168971" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71168971_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71168971" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71168971" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71168971&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71168971" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71168971" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>11</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71168971" src="static/image/common/online_member.gif" />
    <em id="authorposton71168971">发表于 2020-4-27 18:21:10</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71168971" id="qrcode71168971" onclick="qrcodeDisplay(this.href, 'qrcode71168971');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71168971">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71168971" class="cm">
    </div>
    <div id="post_rate_div_71168971"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71168971', 'misc.php?mod=report&rtype=post&rid=71168971&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71186197"><table id="pid71186197" summary="pid71186197" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71186197" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71186197_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71186197')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71186197" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71186197_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71186197" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71186197_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71186197" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71186197" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71186197&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71186197" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71186197" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>12</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71186197" src="static/image/common/online_member.gif" />
    <em id="authorposton71186197">发表于 2020-4-29 18:06:46</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71186197" id="qrcode71186197" onclick="qrcodeDisplay(this.href, 'qrcode71186197');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71186197">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71186197" class="cm">
    </div>
    <div id="post_rate_div_71186197"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71186197', 'misc.php?mod=report&rtype=post&rid=71186197&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71193277"><table id="pid71193277" summary="pid71193277" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71193277" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71193277_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71193277')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71193277" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71193277_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71193277" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71193277_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71193277" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71193277" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71193277&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71193277" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71193277" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>13</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71193277" src="static/image/common/online_member.gif" />
    <em id="authorposton71193277">发表于 2020-4-30 13:49:16</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71193277" id="qrcode71193277" onclick="qrcodeDisplay(this.href, 'qrcode71193277');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71193277">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71193277" class="cm">
    </div>
    <div id="post_rate_div_71193277"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71193277', 'misc.php?mod=report&rtype=post&rid=71193277&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71204010"><table id="pid71204010" summary="pid71204010" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71204010" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71204010_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71204010')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71204010" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71204010_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71204010" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71204010_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71204010" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71204010" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71204010&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71204010" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71204010" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>14</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71204010" src="static/image/common/online_member.gif" />
    <em id="authorposton71204010">发表于 2020-5-1 15:55:39</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71204010" id="qrcode71204010" onclick="qrcodeDisplay(this.href, 'qrcode71204010');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71204010">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71204010" class="cm">
    </div>
    <div id="post_rate_div_71204010"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71204010', 'misc.php?mod=report&rtype=post&rid=71204010&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71207003"><table id="pid71207003" summary="pid71207003" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71207003" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71207003_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71207003')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71207003" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71207003_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71207003" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71207003_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71207003" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71207003" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71207003&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71207003" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71207003" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>15</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71207003" src="static/image/common/online_member.gif" />
    <em id="authorposton71207003">发表于 2020-5-1 21:00:40</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71207003" id="qrcode71207003" onclick="qrcodeDisplay(this.href, 'qrcode71207003');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71207003">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71207003" class="cm">
    </div>
    <div id="post_rate_div_71207003"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71207003', 'misc.php?mod=report&rtype=post&rid=71207003&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71209404"><table id="pid71209404" summary="pid71209404" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71209404" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71209404_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71209404')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71209404" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71209404_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71209404" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71209404_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71209404" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71209404" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71209404&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71209404" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71209404" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>16</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71209404" src="static/image/common/online_member.gif" />
    <em id="authorposton71209404">发表于 2020-5-2 08:56:37</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71209404" id="qrcode71209404" onclick="qrcodeDisplay(this.href, 'qrcode71209404');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71209404">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71209404" class="cm">
    </div>
    <div id="post_rate_div_71209404"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71209404', 'misc.php?mod=report&rtype=post&rid=71209404&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71214587"><table id="pid71214587" summary="pid71214587" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71214587" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71214587_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71214587')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71214587" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71214587_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71214587" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71214587_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71214587" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71214587" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71214587&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71214587" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71214587" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>17</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71214587" src="static/image/common/online_member.gif" />
    <em id="authorposton71214587">发表于 2020-5-2 18:02:53</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71214587" id="qrcode71214587" onclick="qrcodeDisplay(this.href, 'qrcode71214587');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71214587">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71214587" class="cm">
    </div>
    <div id="post_rate_div_71214587"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71214587', 'misc.php?mod=report&rtype=post&rid=71214587&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71220497"><table id="pid71220497" summary="pid71220497" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71220497" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71220497_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71220497')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71220497" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71220497_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71220497" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71220497_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71220497" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71220497" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71220497&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71220497" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71220497" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>18</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71220497" src="static/image/common/online_member.gif" />
    <em id="authorposton71220497">发表于 2020-5-3 12:02:50</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71220497" id="qrcode71220497" onclick="qrcodeDisplay(this.href, 'qrcode71220497');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71220497">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71220497" class="cm">
    </div>
    <div id="post_rate_div_71220497"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71220497', 'misc.php?mod=report&rtype=post&rid=71220497&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71226899"><table id="pid71226899" summary="pid71226899" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71226899" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71226899_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71226899')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71226899" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71226899_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71226899" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71226899_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71226899" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71226899" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71226899&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71226899" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71226899" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>19</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71226899" src="static/image/common/online_member.gif" />
    <em id="authorposton71226899">发表于 2020-5-3 22:57:29</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71226899" id="qrcode71226899" onclick="qrcodeDisplay(this.href, 'qrcode71226899');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71226899">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71226899" class="cm">
    </div>
    <div id="post_rate_div_71226899"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71226899', 'misc.php?mod=report&rtype=post&rid=71226899&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71229401"><table id="pid71229401" summary="pid71229401" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71229401" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71229401_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71229401')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71229401" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71229401_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71229401" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71229401_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71229401" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71229401" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71229401&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71229401" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71229401" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>20</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71229401" src="static/image/common/online_member.gif" />
    <em id="authorposton71229401">发表于 2020-5-4 10:22:33</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71229401" id="qrcode71229401" onclick="qrcodeDisplay(this.href, 'qrcode71229401');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71229401">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71229401" class="cm">
    </div>
    <div id="post_rate_div_71229401"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71229401', 'misc.php?mod=report&rtype=post&rid=71229401&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71235110"><table id="pid71235110" summary="pid71235110" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71235110" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71235110_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71235110')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71235110" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71235110_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71235110" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71235110_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71235110" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71235110" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71235110&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71235110" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71235110" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>21</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71235110" src="static/image/common/online_member.gif" />
    <em id="authorposton71235110">发表于 2020-5-4 19:56:48</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71235110" id="qrcode71235110" onclick="qrcodeDisplay(this.href, 'qrcode71235110');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71235110">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71235110" class="cm">
    </div>
    <div id="post_rate_div_71235110"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71235110', 'misc.php?mod=report&rtype=post&rid=71235110&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71239011"><table id="pid71239011" summary="pid71239011" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71239011" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71239011_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71239011')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71239011" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71239011_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71239011" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71239011_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71239011" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71239011" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71239011&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71239011" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71239011" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>22</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71239011" src="static/image/common/online_member.gif" />
    <em id="authorposton71239011">发表于 2020-5-5 10:28:56</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71239011" id="qrcode71239011" onclick="qrcodeDisplay(this.href, 'qrcode71239011');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71239011">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71239011" class="cm">
    </div>
    <div id="post_rate_div_71239011"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71239011', 'misc.php?mod=report&rtype=post&rid=71239011&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71248445"><table id="pid71248445" summary="pid71248445" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71248445" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71248445_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71248445')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71248445" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71248445_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71248445" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71248445_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71248445" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71248445" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71248445&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71248445" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71248445" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>23</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71248445" src="static/image/common/online_member.gif" />
    <em id="authorposton71248445">发表于 2020-5-6 10:17:00</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71248445" id="qrcode71248445" onclick="qrcodeDisplay(this.href, 'qrcode71248445');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71248445">
    好房出租！<font class="jammer">9 u% h0 G+ ?+ K) w' E5 F( [</font><br />
    </td></tr></table>
    </div>
    <div id="comment_71248445" class="cm">
    </div>
    <div id="post_rate_div_71248445"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71248445', 'misc.php?mod=report&rtype=post&rid=71248445&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71253492"><table id="pid71253492" summary="pid71253492" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71253492" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71253492_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71253492')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71253492" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71253492_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71253492" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71253492_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71253492" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71253492" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71253492&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71253492" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71253492" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>24</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71253492" src="static/image/common/online_member.gif" />
    <em id="authorposton71253492">发表于 2020-5-6 18:38:47</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71253492" id="qrcode71253492" onclick="qrcodeDisplay(this.href, 'qrcode71253492');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71253492">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71253492" class="cm">
    </div>
    <div id="post_rate_div_71253492"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71253492', 'misc.php?mod=report&rtype=post&rid=71253492&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71261009"><table id="pid71261009" summary="pid71261009" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71261009" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71261009_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71261009')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71261009" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71261009_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71261009" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71261009_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71261009" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71261009" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71261009&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71261009" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71261009" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>25</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71261009" src="static/image/common/online_member.gif" />
    <em id="authorposton71261009">发表于 2020-5-7 14:37:47</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71261009" id="qrcode71261009" onclick="qrcodeDisplay(this.href, 'qrcode71261009');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71261009">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71261009" class="cm">
    </div>
    <div id="post_rate_div_71261009"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71261009', 'misc.php?mod=report&rtype=post&rid=71261009&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71264560"><table id="pid71264560" summary="pid71264560" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71264560" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71264560_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71264560')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71264560" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71264560_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71264560" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71264560_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71264560" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71264560" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71264560&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71264560" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71264560" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>26</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71264560" src="static/image/common/online_member.gif" />
    <em id="authorposton71264560">发表于 2020-5-7 20:36:25</em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71264560" id="qrcode71264560" onclick="qrcodeDisplay(this.href, 'qrcode71264560');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71264560">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71264560" class="cm">
    </div>
    <div id="post_rate_div_71264560"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71264560', 'misc.php?mod=report&rtype=post&rid=71264560&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71270033"><table id="pid71270033" summary="pid71270033" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71270033" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71270033_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71270033')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71270033" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71270033_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71270033" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71270033_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71270033" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71270033" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71270033&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71270033" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71270033" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>27</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71270033" src="static/image/common/online_member.gif" />
    <em id="authorposton71270033">发表于 <span title="2020-5-8 12:29:02">7&nbsp;天前</span></em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71270033" id="qrcode71270033" onclick="qrcodeDisplay(this.href, 'qrcode71270033');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71270033">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71270033" class="cm">
    </div>
    <div id="post_rate_div_71270033"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71270033', 'misc.php?mod=report&rtype=post&rid=71270033&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71275607"><table id="pid71275607" summary="pid71275607" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71275607" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71275607_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71275607')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71275607" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71275607_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71275607" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71275607_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71275607" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71275607" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71275607&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71275607" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71275607" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>28</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71275607" src="static/image/common/online_member.gif" />
    <em id="authorposton71275607">发表于 <span title="2020-5-8 21:08:51">7&nbsp;天前</span></em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71275607" id="qrcode71275607" onclick="qrcodeDisplay(this.href, 'qrcode71275607');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71275607">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71275607" class="cm">
    </div>
    <div id="post_rate_div_71275607"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71275607', 'misc.php?mod=report&rtype=post&rid=71275607&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71279385"><table id="pid71279385" summary="pid71279385" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71279385" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71279385_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71279385')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71279385" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71279385_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71279385" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71279385_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71279385" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71279385" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71279385&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71279385" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71279385" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>29</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71279385" src="static/image/common/online_member.gif" />
    <em id="authorposton71279385">发表于 <span title="2020-5-9 10:57:02">6&nbsp;天前</span></em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71279385" id="qrcode71279385" onclick="qrcodeDisplay(this.href, 'qrcode71279385');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71279385">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71279385" class="cm">
    </div>
    <div id="post_rate_div_71279385"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71279385', 'misc.php?mod=report&rtype=post&rid=71279385&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div><div id="post_71284997"><table id="pid71284997" summary="pid71284997" cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls" rowspan="2">
    <div class="pi">
    <div class="authi"><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xw1">汤圆</a>

    </div>
    </div>
    <div class="p_pop blk bui" id="userinfo71284997" style="display: none; margin-top: -11px;">
    <div class="m z">
    <div id="userinfo71284997_ma"></div>
    </div>
    <div class="i y">
    <div>
    <strong><a href="home.php?mod=space&amp;uid=292199" target="_blank" class="xi2">汤圆</a></strong>
    <em>当前在线</em>
    </div>
    <dl class="cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>分享</dt><dd><a href="home.php?mod=space&uid=292199&do=share&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>记录</dt><dd><a href="home.php?mod=space&uid=292199&do=doing&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>相册</dt><dd><a href="home.php?mod=space&uid=292199&do=album&view=me&from=space" target="_blank" class="xi2">5</a></dd><dt>好友</dt><dd><a href="home.php?mod=space&uid=292199&do=friend&view=me&from=space" target="_blank" class="xi2">1</a></dd><dt>日志</dt><dd><a href="home.php?mod=space&uid=292199&do=blog&view=me&from=space" target="_blank" class="xi2">0</a></dd><dt>在线时间</dt><dd>797 小时</dd><dt>注册时间</dt><dd>2011-8-5</dd><dt>阅读权限</dt><dd>20</dd><dt>最后登录</dt><dd>2020-5-15</dd></dl>
    <div class="imicn">
    <a href="home.php?mod=space&amp;uid=292199&amp;do=profile" target="_blank" title="查看详细资料"><img src="static/image/common/userinfo.gif" alt="查看详细资料" /></a>
    </div>
    <div id="avatarfeed"><span id="threadsortswait"></span></div>
    </div>
    </div>
    <div>
    <div class="avatar" onmouseover="showauthor(this, 'userinfo71284997')"><a href="home.php?mod=space&amp;uid=292199" target="_blank"><img src="http://u.skykiwi.com/avatar.php?uid=292199&size=middle" /></a></div>
    <p><em><a href="home.php?mod=spacecp&amp;ac=usergroup&amp;gid=39" target="_blank">长 老 级</a></em></p>
    </div>
    <p id="g_up71284997" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><img src="static/image/common/star_level3.gif" alt="Rank: 8" /><img src="static/image/common/star_level3.gif" alt="Rank: 8" /></p>
    <div id="g_up71284997_menu" class="tip tip_4" style="display: none;">
    <div class="tip_horn"></div>
    <div class="tip_c">长 老 级, 积分 805, 距离下一级还需 195 积分</div>
    </div>
    <p id="plgup71284997" onmouseover="showMenu({'ctrlid':this.id, 'pos':'12!'});"><span style="float:left;">升级&nbsp;</span><span style="padding-top:4px;float:left;"><img width="2" height="12" src="source/plugin/plbeautify/images/expl.gif"><img width="29.28" height="12" src="source/plugin/plbeautify/images/expc.gif"><img width="6" height="12" src="source/plugin/plbeautify/images/expr.gif"></span>&nbsp;<span>61%</span></p><div id="plgup71284997_menu" class="tip tip_4" style="position: absolute; z-index: 301; left: 215px; top: 771px; display: none; "><div class="tip_horn"></div><div class="tip_c">当前用户组为 <span style="color:red;">长 老 级</span><br />当前积分为 <span style="color:red;">805</span>, 升到下一级还需要 195 点。</div></div><dl class="pil cl"><dt>UID</dt><dd>292199</dd><dt>热情</dt><dd>106 </dd><dt>人气</dt><dd>891 </dd><dt>主题</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=thread&view=me&from=space" target="_blank" class="xi2">57</a></dd><dt>帖子</dt><dd><a href="home.php?mod=space&uid=292199&do=thread&type=reply&view=me&from=space" target="_blank" class="xi2">540</a></dd><dt>精华</dt><dd>0</dd><dt>积分</dt><dd>805</dd><dt>阅读权限</dt><dd>20</dd><dt>注册时间</dt><dd>2011-8-5</dd></dl><ul class="xl xl2 o cl">
    <li class="callon"><a href="home.php?mod=space&amp;uid=292199" target="_blank" title="串个门" class="xi2">串个门</a></li>
    <li class="buddy"><a href="home.php?mod=spacecp&amp;ac=friend&amp;op=add&amp;uid=292199&amp;handlekey=addfriendhk_292199" id="a_friend_li_71284997" onclick="showWindow(this.id, this.href, 'get', 1, {'ctrlid':this.id,'pos':'00'});" title="加好友" class="xi2">加好友</a></li>
    <li class="poke2"><a href="home.php?mod=spacecp&amp;ac=poke&amp;op=send&amp;uid=292199" id="a_poke_li_71284997" onclick="showWindow(this.id, this.href, 'get', 0);" title="打招呼" class="xi2">打招呼</a></li>
    <li class="pm2"><a href="home.php?mod=spacecp&amp;ac=pm&amp;op=showmsg&amp;handlekey=showmsg_292199&amp;touid=292199&amp;pmid=0&amp;daterange=2&amp;pid=71284997&amp;tid=3896975" onclick="showWindow('sendpm', this.href);" title="发消息" class="xi2">发消息</a></li>
    </ul>
    </td>
    <td class="plc">
    <div class="pi">
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71284997" title="您的朋友访问此链接后，您将获得相应的积分奖励" id="postnum71284997" onclick="setCopy(this.href, '帖子地址复制成功');return false;"><em>30</em>#分享本帖地址</a>
    </strong>
    <div class="pti">
    <div class="pdbt">
    </div>
    <div class="authi">
    <img class="authicn vm" id="authicon71284997" src="static/image/common/online_member.gif" />
    <em id="authorposton71284997">发表于 <span title="2020-5-9 21:23:43">6&nbsp;天前</span></em>
    <span class="xg1">来自手机</span>
    <span class="pipe">|</span><a href="forum.php?mod=viewthread&amp;tid=3896975&amp;page=1&amp;authorid=292199" rel="nofollow">只看该作者</a>
    <strong>
    <a href="forum.php?mod=redirect&goto=findpost&ptid=3896975&pid=71284997" id="qrcode71284997" onclick="qrcodeDisplay(this.href, 'qrcode71284997');return false;" style="color:#679a07; font-weight:bold; background-image:url(../../static/image/common/weixinlogo.png); background-repeat:no-repeat; background-size: 20px; background-position: 8%; width:56px; padding-left:28px; line-height:19px; float:none;">微信分享</a>
    </strong>
    </div>
    </div>
    </div><div class="pct"><div class="pcb">
    <div class="t_fsz">
    <table cellspacing="0" cellpadding="0"><tr><td class="t_f" id="postmessage_71284997">
    好房出租！</td></tr></table>
    </div>
    <div id="comment_71284997" class="cm">
    </div>
    <div id="post_rate_div_71284997"></div>
    </div></div>

    </td></tr>
    <tr><td class="plc plm">
    </td>
    </tr>
    <tr>
    <td class="pls"></td>
    <td class="plc">
    <div class="po">
    <div class="pob cl">
    <em>
    </em>

    <p>
    <a href="javascript:;" onclick="showWindow('miscreport71284997', 'misc.php?mod=report&rtype=post&rid=71284997&tid=3896975&fid=19', 'get', -1);return false;">举报</a>
    </p>

    </div>
    </div>

    </td>
    </tr>
    <tr class="ad">
    <td class="pls"></td>
    <td class="plc">
    </td>
    </tr>
    </table>
    </div>
    <div id="postlistreply" class="pl"><div id="post_new" class="viewthread_table" style="display: none"></div></div>
    </div>


    <form method="post" autocomplete="off" name="modactions" id="modactions">
    <input type="hidden" name="formhash" value="cec12cfe" />
    <input type="hidden" name="optgroup" />
    <input type="hidden" name="operation" />
    <input type="hidden" name="listextra" value="page%3D1%26filter%3Dsortid%26sortid%3D287" />
    <input type="hidden" name="page" value="1" />
    </form>


    <div class="pgs mtm mbm cl">
    <div class="pg"><strong>1</strong><a href="forum.php?mod=viewthread&tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;page=2">2</a><a href="forum.php?mod=viewthread&tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;page=2" class="nxt">下一页</a></div><span class="pgb y" id="visitedforumstmp" onmouseover="$('visitedforums').id = 'visitedforumstmp';this.id = 'visitedforums';showMenu({'ctrlid':this.id,'pos':'21'})"><a href="forum.php?mod=forumdisplay&fid=19&page=1&filter=sortid&sortid=287">返回列表</a></span>
    <a id="newspecialtmp" data-reply-archiveid="int(0)
    " data-reply-allow="bool(false)
    " onmouseover="$('newspecial').id = 'newspecialtmp';this.id = 'newspecial';showMenu({'ctrlid':this.id})" onclick="location.href='forum.php?mod=post&action=newthread&fid=19';return false;" href="javascript:;" title="发新帖"><img src="static/image/common/pn_post.png" alt="发新帖" /></a></div>

    <!--[diy=diyfastposttop]--><div id="diyfastposttop" class="area"><div id="framefq8Iys" class=" frame move-span cl frame-1"><div id="framefq8Iys_left" class="column frame-1-c"><div id="framefq8Iys_left_temp" class="move-span temp"></div><div id="portal_block_279" class="block move-span"><div id="portal_block_279_content" class="dxb_bc"><div class="portal_block_summary"><script type='text/javascript'><!--//<![CDATA[
    document.MAX_ct0 = unescape('INSERT_ENCODED_CLICKURL_HERE');

    var m3_u = (location.protocol=='https:'?'https://interactives.skykiwi.com/www/delivery/ajs.php':'http://interactives.skykiwi.com/www/delivery/ajs.php');
    var m3_r = Math.floor(Math.random()*99999999999);
    if (!document.MAX_used) document.MAX_used = ',';
    document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
    document.write ("?zoneid=59");
    document.write ('&amp;cb=' + m3_r);
    if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
    document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
    document.write ("&amp;loc=" + escape(window.location));
    if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
    if (document.context) document.write ("&context=" + escape(document.context));
    if ((typeof(document.MAX_ct0) != 'undefined') && (document.MAX_ct0.substring(0,4) == 'http')) {
        document.write ("&amp;ct0=" + escape(document.MAX_ct0));
    }
    if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
    document.write ("'></scr"+"ipt>");
    //]]>--></script><noscript><a href='http://interactives.skykiwi.com/www/delivery/ck.php?n=a4099994&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://interactives.skykiwi.com/www/delivery/avw.php?zoneid=59&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=a4099994&amp;ct0=INSERT_ENCODED_CLICKURL_HERE' border='0' alt='' /></a></noscript></div></div></div></div></div></div><!--[/diy]-->
    <script type="text/javascript">
    var postminchars = parseInt('15');
    var postmaxchars = parseInt('53000');
    var disablepostctrl = parseInt('0');
    </script>

    <div id="f_pst" class="pl bm bmw">
    <form method="post" autocomplete="off" id="fastpostform" action="forum.php?mod=post&amp;action=reply&amp;fid=19&amp;tid=3896975&amp;extra=page%3D1%26filter%3Dsortid%26sortid%3D287&amp;replysubmit=yes&amp;infloat=yes&amp;handlekey=fastpost" onSubmit="return fastpostvalidate(this)">
    <table cellspacing="0" cellpadding="0">
    <tr>
    <td class="pls">
    </td>
    <td class="plc">

    <span id="fastpostreturn"></span>


    <div class="cl">
    <div id="fastsmiliesdiv" class="y"><div id="fastsmiliesdiv_data"><div id="fastsmilies"></div></div></div><div class="hasfsl" id="fastposteditor">
    <div class="tedt mtn">
    <div class="bar">
    <span class="y">
    <a href="forum.php?mod=post&amp;action=reply&amp;fid=19&amp;tid=3896975" onclick="return switchAdvanceMode(this.href)">高级模式</a>
    </span><script src="static/js/seditor.js?anl" type="text/javascript"></script>
    <div class="fpd">
    <a href="javascript:;" title="文字加粗" class="fbld">B</a>
    <a href="javascript:;" title="设置文字颜色" class="fclr" id="fastpostforecolor">Color</a>
    <a id="fastpostimg" href="javascript:;" title="图片" class="fmg">Image</a>
    <a id="fastposturl" href="javascript:;" title="添加链接" class="flnk">Link</a>
    <a id="fastpostquote" href="javascript:;" title="引用" class="fqt">Quote</a>
    <a id="fastpostcode" href="javascript:;" title="代码" class="fcd">Code</a>
    <a href="javascript:;" class="fsml" id="fastpostsml">Smilies</a>
    </div></div>
    <div class="area">
    <!-- <div class="pt hm">您需要登录后才可以回帖 <a href="member.php?mod=logging&amp;action=login" onclick="showWindow('login', this.href)" class="xi2">登录</a> | <a href="member.php?mod=register2013" class="xi2">注册</a></div> -->
    <div class="pt hm">您需要登录后才可以回帖 <a href="https://passport.skykiwi.com/v1/login/bbslogon.do">登录</a> | <a href="https://passport.skykiwi.com/v1/login/bbslogon.do">注册</a> </div>
    </div>
    </div>
    </div>
    </div>


    <input type="hidden" name="formhash" value="cec12cfe" />
    <input type="hidden" name="subject" value="" />
    <p class="ptm pnpost">
    <button type="button" onclick="showWindow('login', 'member.php?mod=logging&action=login&guestmessage=yes')" name="replysubmit" id="fastpostsubmit" class="pn pnc vm" value="replysubmit" tabindex="5"><strong>发表回复</strong></button>
    <label for="fastpostrefresh"><input id="fastpostrefresh" type="checkbox" class="pc" />回帖后跳转到最后一页</label>
    <script type="text/javascript">if(getcookie('fastpostrefresh') == 1) {$('fastpostrefresh').checked=true;}</script>
    </p>
    </td>
    </tr>
    </table>
    </form>
    </div>


    <div id="visitedforums_menu" class="p_pop blk cl" style="display: none;">
    <table cellspacing="0" cellpadding="0">
    <tr>
    <td id="v_forums">
    <h3 class="mbn pbn bbda xg1">浏览过的版块</h3>
    <ul class="xl xl1">
    <li><a href="forum.php?mod=forumdisplay&fid=247">谈房说地</a></li><li><a href="forum.php?mod=forumdisplay&fid=55">求职招聘</a></li><li><a href="forum.php?mod=forumdisplay&fid=53">§§数码之家§§</a></li></ul>
    </td>
    </tr>
    </table>
    </div>
    <script type="text/javascript">document.onkeyup = function(e){keyPageScroll(e, 0, 1, 'forum.php?mod=viewthread&tid=3896975', 1);}</script>
    </div>

    <div class="wp mtn">
    <!--[diy=diy3]--><div id="diy3" class="area"><div id="frameCFhY1F" class=" frame move-span cl frame-1"><div id="frameCFhY1F_left" class="column frame-1-c"><div id="frameCFhY1F_left_temp" class="move-span temp"></div><div id="portal_block_251" class="block move-span"><div id="portal_block_251_content" class="dxb_bc"><div class="portal_block_summary"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <!-- 横幅自适应 -->
    <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-2607075201193380"
        data-ad-slot="4897960190"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script></div></div></div></div></div></div><!--[/diy]-->
    </div>

    <div id="qrcode_menu" class="p_pop blk" style="display: none; width:150px;">
    <input type="hidden" name="ctrl_id_qrcode_menu" id="ctrl_id_qrcode_menu" value="none" />
    <img id="img_qrcode_in_menu" src="" border="0" width="150px">
    </div>


    <script type="text/javascript">

    function qrcodeDisplay(href, itemid){
    var obj_img_qrcode_in_menu = $('img_qrcode_in_menu');
    if (! obj_img_qrcode_in_menu){
    return false;
    }

    var obj_ctrl_id_qrcode_menu = $('ctrl_id_qrcode_menu');

    if (obj_ctrl_id_qrcode_menu.value == ''){
    obj_ctrl_id_qrcode_menu.value = 'none';
    hideMenu('qrcode_menu');
    }else{
    obj_ctrl_id_qrcode_menu.value = '';
    obj_img_qrcode_in_menu.src = 'misc.php?mod=qrcode&action=gen&text='+encodeURIComponent(href);

    showMenu({'ctrlid':itemid, 'menuid':'qrcode_menu','pos':'34!','ctrlclass':'a','duration':3});

    }

    }

    </script>


        </div>
    <div id="ft" class="wp cl">
    <div id="flk" class="y">
    <p><a href="forum.php?mobile=yes" >手机版</a><span class="pipe">|</span><a href="http://bbs.skykiwi.com/contact.php"  style="font-weight: bold;color: blue">联系论坛客服</a><span class="pipe">|</span><a href="http://em.skykiwi.com" target="_blank"  style="font-weight: bold;text-decoration: underline;">广告服务</a><span class="pipe">|</span><a href="http://em.skykiwi.com/aboutus_join.html" target="_blank"  style="font-weight: bold;text-decoration: underline;">招贤纳士</a><span class="pipe">|</span><strong><a href="http://www.skykiwi.com/" target="_blank">新西兰天维网</a></strong>
    <!-- START: Google Analyse -->
    <script type="text/javascript">
        var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
        document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
    </script>
    <script type="text/javascript">
        try {
        var pageTracker = _gat._getTracker("UA-4716393-5");
        pageTracker._setDomainName("skykiwi.com");
        pageTracker._trackPageview();
        } catch(err) {}
    </script>
    <!-- END: Google Analyse --></p>
    <p class="xs0">
    GMT+12, 2020-5-15 18:44<span id="debuginfo">
    , Processed in 0.027307 second(s), 16 queries
    .
    </span>
    </p>
    </div>
    <div id="frt">
    <p>Powered by <strong><a href="http://www.discuz.net" target="_blank">Discuz!</a></strong> <em>X2</em> <a href="http://license.comsenz.com/?pid=1&amp;host=bbs.skykiwi.com" target="_blank">Licensed</a></p>
    <p class="xs0">&copy; 2001-2011 <a href="http://www.comsenz.com" target="_blank">Comsenz Inc.</a></p>
    </div></div>

    <div id="g_upmine_menu" class="tip tip_3" style="display:none;">
    <div class="tip_c">
    积分 0, 距离下一级还需  积分
    </div>
    <div class="tip_horn"></div>
    </div>
    <span id="scrolltop" onclick="window.scrollTo('0','0')">回顶部</span>
    <script type="text/javascript">_attachEvent(window, 'scroll', function(){showTopLink();});</script>

    </body>
    </html>

"""

#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc,features="lxml")#"html.parser",from_encoding="utf-8")

print ("--标题--")
print(soup.find('a',id="thread_subject").get_text())

imgname = './img1.png'
tables = soup.findAll('table',bordercolor="#fff")
tab = tables[0]
for tr in tab.findAll('tr'):
    for td in tr.findAll('td'):
        if not(td.getText() in ["类型:","每周租金:","微信:","联系电话:"]):
            if td.getText()=="":
               print ("http://bbs.skykiwi.com/"+td.find('image')["src"])
            #    urlretrieve("http://bbs.skykiwi.com/"+td.find('image')["src"], imgname)
            #    phonenum=pytesseract.image_to_string(Image.open(imgname),lang='chi_sim')
            #    print(phonenum)
            #    os.remove(imgname)
            else:
                print (td.getText())

print ("内容")
text = soup.find('td',class_="t_f")
print(text.contents[0].strip())
# for tx in text.contents:
#     if isinstance(tx, str):
#         print(tx.strip())