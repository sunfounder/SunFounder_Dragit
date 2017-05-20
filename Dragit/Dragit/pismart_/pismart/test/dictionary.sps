[ hi | hey | hello | yo | ok ] [ pi smart ];
@results
	0 {'__NAME__'}
@

#forwardAction() = [go] | [run] | [move] | [roll] | [come] | [walk] | [step] | [march] | [head] | [travel] | [advance];
@results
    1 { "go" }
    2 { "run" }
    3 { "move" }
    4 { "roll" }
    5 { "come" }
    6 { "walk" }
    7 { "step" }
    8 { "march" }
    9 { "head" }
    10 { "travel" }
    11 { "advance" }
@

#forwardDir() = [forward] | [forwards] | [ahead] | [along] | [onwards] | [forth] | [towards the front];
@results
    1 { "forward" }
    2 { "forwards" }
    3 { "ahead" }
    4 { "along" }
    5 { "onwards" }
    6 { "forth" }
    7 { "towards the front" }
@

(can you)? (please)? [#forwardAction] [#forwardDir] (please)?;
@results
    #forwardAction, forwardDir { 'forward:' #forwardAction ' ' #forwardDir '' }
@


#leftAction() = [turn] | [go] | [run] | [direct] | [move] | [walk] | [swing] | [divert] | [deflect] | [steer] | [change] | [alter];
@results
    1 { "turn" }
    2 { "go" }
    3 { "run" }
    4 { "direct" }
    5 { "move" }
    6 { "walk" }
    7 { "swing" }
    8 { "divert" }
    9 { "deflect" }
    10 { "steer" }
    11 { "change" }
    12 { "alter" }
@

#leftDir() = [left] | [towards the left] | [left direction] | [to the left];
@results
    1 { "left" }
    2 { "towards the left" }
    3 { "left direction" }
    4 { "to the left" }
@

(can you)? (please)? [#leftAction] [#leftDir] (please)?;
@results
    #leftAction, leftDir { 'left:' #leftAction ' ' #leftDir '' }
@


#rightDir() = [right] | [towards the right] | [right direction] | [to the right];
@results
    1 { "right" }
    2 { "towards the right" }
    3 { "right direction" }
    4 { "to the right" }
@

(can you)? (please)? [#leftAction] [#rightDir] (please)?;
@results
    #leftAction, rightDir { 'right:' #leftAction ' ' #rightDir '' }
@


#backwardAction() = [go] | [run] | [move] | [roll] | [come] | [walk] | [step] | [back] | [rear];
@results
    1 { "go" }
    2 { "run" }
    3 { "move" }
    4 { "roll" }
    5 { "come" }
    6 { "walk" }
    7 { "step" }
    8 { "back" }
    9 { "rear" }
@

#backwardDir() = [backward] | [backwards] | [back] | [towards the back] | [aback] | [behind];
@results
    1 { "backward" }
    2 { "backwards" }
    3 { "back" }
    4 { "towards the back" }
    5 { "aback" }
    6 { "behind" }
@

(can you)? (please)? [#backwardAction] [#backwardDir] (please)?;
@results
    #backwardAction, backwardDir { 'backward:' #backwardAction ' ' #backwardDir '' }
@