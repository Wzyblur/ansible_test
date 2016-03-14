
;(function(){
    if(window.__player_configs){ return; }
    Do.add('json', {path: 'https://img3.doubanio.com/f/music/4dfbab320a2646c97b9a3fab256c81d4c49d83d2/js/music/lib/json.js', type: 'js'});
    Do.add('flash-transport', {path: 'https://img3.doubanio.com/f/music/53106daa360b681b38e4d8ca4cae379e2a9a9cc4/js/music/player/pageconn/flashtransport.js', type: 'js'});
    Do.add('xdm-transport', {path: 'https://img3.doubanio.com/f/music/e0c59262a5d370deb35f338cd4872a00ed804263/js/music/player/pageconn/xdmtransport.js', type: 'js'});
    Do.add('jstorage-transport', {path: 'https://img3.doubanio.com/f/music/da39a3ee5e6b4b0d3255bfef95601890afd80709/js/music/player/pageconn/jstoragetransport.js', type: 'js'});
    var isSafari = typeof window.navigator !== 'undefined' && window.navigator.vendor === 'Apple Computer, Inc.';
    var supportTouch = ('ontouchstart' in document.documentElement);
    var transport, requires = [];
    if(isSafari && !supportTouch) {
        transport = 'flash';
        requires.push('flash-transport');
    } else {
        transport = 'easyxdm';
        requires.push('xdm-transport');
    }
    if(!window.JSON){
        requires.push('json');
    }
    window.__player_configs = {
        remote: window.location.protocol + '//music.douban.com/artists/player/xdmserver',
        conn_client: '/swf/53025/conn_client.swf',
        source: 'anony_page',
        douban_music: window.location.protocol + '//music.douban.com'
    };
    Do.add('artistplayer', {
        path: 'https://img3.doubanio.com/f/music/f73a1d2c5cfdf3caa990814d0e02c63e892d09ae/js/music/player/pageconn/client.js',
        type: 'js',
        requires: requires
    });
})();

Do(function() {
if (($.browser.version|0) < 9 && $.browser.msie) {
  $('.section:nth-child(2n)').addClass('section-bg');
}
});
Do.ready(function(){
  var lazyPic={counter:0,areas:[],add:function(){if(arguments.length===0){return}this.areas=this.areas.concat(Array.prototype.slice.apply(arguments));this.counter=this.areas.length},check:function(){if(this.counter===0){return}var b=this;var a=document.body.scrollTop||document.documentElement.scrollTop;$.each(this.areas,function(e,f){if(!f){return}var d=$(f);if(d.length===0){return}var h=d.offset().top;var g=h+d.height();var c=window.innerHeight||document.documentElement.clientHeight;if(h>a&&h<a+c||g>a&&g<a+c){b.areas[e]=null;b.counter--;b.load(f)}})},load:function(a){var b=$(a).find("img[data-origin]");$.each(b,function(d,c){c.setAttribute("src",c.getAttribute("data-origin"))})}};$(window).bind("scroll",function _loadpic(){var a;return function(){if(a){window.clearTimeout(a)}a=window.setTimeout(function(){lazyPic.check()},100)}}()).trigger("scroll");
  lazyPic.add('#anony-sns',
  '#anony-movie',
  '#anony-book',
  '#anony-music',
  '#anony-group',
  '#anony-events');

  var input_label=function(c,a){if("placeholder" in document.createElement("input")){return}if(!a){a=c.parent()}var b=$('<label class="label">'+c.attr("placeholder")+"</label>").prependTo(c.parent());c.attr("placeholder","");b.click(function(){c.focus()});if(c.val()){a.addClass("inp-focus")}c.bind({focus:function(){a.addClass("inp-focus")},blur:function(){if(this.value==""){a.removeClass("inp-focus")}}})};
  input_label($('#anony-nav').find('.inp input'),
              $('#anony-nav').find('.anony-srh'));

  var account = $('#lzform').find('.item-account');
  input_label(account.find('input:eq(0)'), account);

  var passwd = $('#lzform').find('.item-passwd');
  input_label(passwd.find('input'), passwd);

  var captcha = $('#lzform').find('.item-captcha');
  if (captcha.length) {
    input_label(captcha.find('input'), captcha);
  }

  if (account.find('input').val()) {
    passwd.find('input').focus();
  }

  Do.preload(['https://img3.doubanio.com/f/shire/0a62663763aed4fe860029f99d1755b8caa524e7/js/separation/_all.js','https://img3.doubanio.com/f/shire/07f5c81e9c7fcdd676bf2078c79d6c5ffbb93b80/js/douban.js']);

  Do('artistplayer', function () {
    var isPlayerLoaded = false;
    artistsPlayer.ready(function(artistsPlayer, hasPlayer){
      isPlayerLoaded = true;
    });
    $('.artist-song-play').hover(
      function () {
        $(this).toggleClass('hover');
      }
    ).click(
      function () {
        var sids = $(this).data('sids');
        if (isPlayerLoaded && sids && sids.length > 0) {
          artistsPlayer.play(sids, {source: 'anony_page'});
        }
      }
    );
  });
});
