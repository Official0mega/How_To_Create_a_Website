#include <iostream>
int main()
{


Learn CSS!


Search
000
Learn CSS
001
Box Model
002
Selectors
003
The cascade
004
Specificity
005
Inheritance
006
Color
007
Sizing Units
008
Layout
009
Flexbox
010
Grid
011
Logical Properties
012
Spacing
013
Pseudo-elements
014
Pseudo-classes
015
Borders
016
Shadows
017
Focus
018
Z-index and stacking contexts
019
Functions
020
Gradients
021
Animations
022
Filters
023
Blend Modes
024
Lists
025
Transitions
026
Overflow
027
Backgrounds
028
Text and typography
029
Conclusion and next steps
Learn
Learn CSS!
Share
021
Animations
Animation is a great way to highlight interactive elements, and add interest and fun to your designs. In this module find out how to add and control animation effects with CSS.

On this page
What is a keyframe?
@keyframes
The animation properties
animation-duration
animation-timing-function
animation-iteration-count
animation-direction
animation-delay
animation-play-state
animation-fill-mode
The animation shorthand
Considerations when working with animation


The CSS Podcast - 022: Animation
Sometimes you see little helpers on interfaces that when clicked, provide some helpful information about that particular section. These often have a pulsing animation to subtly let you know that the information is there and should be interacted with. How do you do this with CSS though?


In CSS, you can make this type of animation using CSS animations, which allow you to set an animation sequence, using keyframes. Animations can be simple, one state animations, or even complex, time-based sequences.

What is a keyframe? #
In animation software, CSS, and most other tools that enable you to animate something, keyframes are the mechanism that you use to assign animation states to timestamps, along a timeline.

Let's use the "pulser" as a context for this. The entire animation runs for 1 second and runs over 2 states.

The states of the pulser animation over the 1 second timeframe
There's a specific point where each of these animation states start and end. You map these out on the timeline with keyframes.

The same diagram as before, but this time, with keyframes
@keyframes #
Browser support
43
16
12
9
Source
Now you know what a keyframe is, that knowledge should help you understand how the CSS @keyframes rule works. Here is a basic rule with two states.


@keyframes my-animation {
	from {
		transform: translateY(20px);
	}
	to {
		transform: translateY(0px);
	}
}
The first part to note is the custom ident (custom identifier)—or in more human terms, the name of the keyframes rule. This rule's identifier is my-animation. The custom identifier works like a function name. Which, as you learned in the functions module, lets you reference the keyframes rule elsewhere in your CSS code.

A <custom-ident> is used in various places in CSS, and allows you to provide your own name for things. These identifiers are case-sensitive, and in some cases there are words that you can't use. For example, when naming lines in CSS Grid, you can't use the word span.
Inside the keyframes rule, from and to are keywords that represent 0% and 100%, which are the start of the animation and end. You could re-create the same rule like this:


@keyframes my-animation {
	0% {
		transform: translateY(20px);
	}
	100% {
		transform: translateY(0px);
	}
}
You can add as many positions as you like along the timeframe. Using the context of the "pulser" example, there are 2 states, which translate to 2 keyframes. This means you have 2 positions inside your keyframes rule to represent the changes for each of these keyframes.


@keyframes pulse {
  0% {
    opacity: 0;
  }
  50% {
    transform: scale(1.4);
    opacity: 0.4;
  }
}

The animation properties #
Browser support
43
16
12
9
Source
To use your @keyframes in a CSS rule, define various animation properties or, use the animation shorthand property.

animation-duration #
Browser support
43
16
12
9
Source

.my-element {
	animation-duration: 10s;
}
The animation-duration property defines how long the @keyframes timeline should be. It should be a time value. It defaults to 0 seconds, which means the animation still runs, but it'll be too quick for you to see. You can't add negative time values.

animation-timing-function #
Browser support
43
16
12
9
Source
To help recreate natural motion in animation, you can use timing functions that calculate the speed of an animation at each point. Calculated values are often curved, making the animation run at variable speeds over the course of animation-duration, and if a value is calculated beyond that of the value defined in @keyframes, make the element appear to bounce.

There are several keywords available as presets in CSS, which are used as the value for animation-timing-function: linear, ease, ease-in, ease-out, ease-in-out.


.my-element {
	animation-timing-function: ease-in-out;
}

Values appear to curve with easing functions because easing is calculated using a bézier curve, which is used to model velocity. Each of the timing function keywords, such as ease, reference a pre-defined bézier curve. In CSS, you can define a bézier curve directly, using the cubic-bezier() function, which accepts four number values: x1, y1, x2, y2.


.my-element {
	animation-timing-function: cubic-bezier(.42, 0, .58, 1);
}
These values plot each part of the curve along the X and Y axis.

A bézier on a progression vs time chart
Understanding bézier curves is complicated and visual tools, such as this generator by Lea Verou are very helpful.

The steps easing function #
Sometimes you might want more granular control of your animation, and instead of moving along a curve, you want to move in intervals instead. The steps() easing function lets you break the timeline into defined, equal intervals.


.my-element {
	animation-timing-function: steps(10, end);
}
The first argument is how many steps. If steps are defined as 10 and there are 10 keyframes, each keyframe will play in sequence for the exact amount of time, with no transition between states. If there are not enough keyframes for the steps, steps between keyframes are added depending on the second argument.

The second argument is the direction. If it's set to end, which is the default, the steps finish at the end of your timeline. If it is set to start, the first step of your animation completes as soon as it starts, which means it ends one step earlier than end.


animation-iteration-count #
Browser support
43
16
12
9
Source

.my-element {
	animation-iteration-count: 10;
}
The animation-iteration-count property defines how many times the @keyframes timeline should run. By default, this is 1, which means that when the animation reaches the end of your timeline, it will stop at the end. The number can't be a negative number.


You can use the infinite keyword which will loop your animation, which is how the "pulser" demo from the start of this lesson works.


animation-direction #
Browser support
43
16
12
9
Source

.my-element {
	animation-direction: reverse;
}
You can set which direction the timeline runs over your keyframes with animation-direction:

normal: the default value, which is forwards.
reverse: runs backwards over your timeline.
alternate: for each animation iteration, the timeline will run forwards or backwards in sequence.
alternate-reverse: the reverse of alternate.

animation-delay #
Browser support
43
16
12
9
Source

.my-element {
	animation-delay: 5s;
}
The animation-delay property defines how long to wait before starting the animation. Like the animation-duration property, this accepts a time value.

Unlike the animation-duration property, you can define this as a negative value. If you set a negative value, the timeline in your @keyframes will start at that point. For example, if your animation is 10 seconds long and you set animation-delay to -5s, it will start from half-way along your timeline.


animation-play-state #
Browser support
43
16
12
9
Source

.my-element:hover {
	animation-play-state: paused;
}
The animation-play-state property allows you to play and pause the animation. The default value is running and if you set it to paused, it will pause the animation.


animation-fill-mode #
Browser support
43
16
12
9
Source
The animation-fill-mode property defines which values in your @keyframes timeline persist before the animation starts or after it ends. The default value is none which means when the animation is complete, the values in your timeline are discarded. Other options are:

forwards: The last keyframe will persist, based on the animation direction.
backwards: The first keyframe will persist, based on the animation direction.
both: follows the rules for both forwards and backwards.

The animation shorthand #
Instead of defining all the properties separately, you can define them in an animation shorthand, which lets you define the animation properties in the following order:

animation-name
animation-duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction
animation-fill-mode
animation-play-state

.my-element {
	animation: my-animation 10s ease-in-out 1s infinite forwards forwards running;
}
Considerations when working with animation #
Users can define in their operating system that they prefer to reduce motion experienced when they interact with applications and websites. This preference can be detected using the prefers-reduced-motion media query.


@media (prefers-reduced-motion) {
  .my-autoplaying-animation {
    animation-play-state: paused;
  }
}
This isn't necessarily a preference of no animation, but rather, a preference to reduce animations— especially unexpected ones. You can learn more about this preference and overall performance with this animation guide.


Check your understanding
Test your knowledge of animations
QUESTION 1
QUESTION 2
QUESTION 3
QUESTION 4
The name or custom identifier of a @keyframes animation is case sensitive?



True

False
CHECK
PREV
020
Gradients
NEXT
022
Filters
Filters in CSS mean that you can apply effects you might only think possible in a graphics application. In this module, you can discover what is available.

We want to help you build beautiful, accessible, fast, and secure websites that work cross-browser, and for all of your users. This site is our home for content to help you on that journey, written by members of the Chrome team, and external experts.

Contribute
File a bug
View source
Related content
developer.chrome.com
Chrome updates
Case studies
Podcasts
Shows
Connect
Twitter
YouTube
Google Developers
Chrome
Firebase
Google Cloud Platform
All products
Dark theme


ENGLISH (en)
Terms & Privacy
Community Guidelines
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies.

By
Chrome DevRel
}
