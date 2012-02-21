$(document).ready(function() {
    if ($('.video')[0] !== undefined){
        flowplayer("a.video", "++resource++s17.media.views/flowplayer/flowplayer-3.2.7.swf");
    }

    // install flowplayer into container
    if ($('.audio')[0] !== undefined){
        flowplayer("a.audio", "++resource++s17.media.views/flowplayer/flowplayer-3.2.7.swf", {

            // fullscreen button not needed here
            plugins: {
                controls: {
                    fullscreen: false,
                    height: 30,
                    autoHide: false
                }
            },

            clip: {
                autoPlay: false,

                // optional: when playback starts close the first audio playback
                onBeforeBegin: function() {
                    $f("player").close();
                }
            }
        });    
    }
});
