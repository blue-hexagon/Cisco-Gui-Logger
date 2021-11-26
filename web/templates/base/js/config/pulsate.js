function showActiveElement(elem) {
    /* Highlight element that is jumped to, when clicking a #targetLink on the same page.
    * This code places a blue border for close to 1 second, around the target that is jumped to. */
    $("#" + elem).pulsate({
        color: "#3498DB", // set the color of the pulse
        reach: 1,                              // how far the pulse goes in px
        speed: 751,                            // how long one pulse takes in ms
        pause: 0,                               // how long the pause between pulses is in ms
        glow: false,                             // if the glow should be shown too
        repeat: 0,                           // will repeat forever if true, if given a number will repeat for that many times
        onHover: false                          // if true only pulsate if user hovers over the element
    });
}