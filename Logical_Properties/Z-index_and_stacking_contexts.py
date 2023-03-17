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
018
Z-index and stacking contexts
In this module find out how to control the order in which things layer on top of each other, by using z-index and the stacking context.

On this page
Z-index
Negative z-index
Stacking context
Creating a stacking context
Resources


The CSS Podcast - 019: z-index and stacking contexts
Say you've got a couple of elements that are absolutely positioned, and are supposed to be positioned on top of each other. You might write a bit of a HTML like this:


<div class="stacked-items">
	<div class="item-1">Item 1</div>
	<div class="item-2">Item 2</div>
</div>
But which one sits on top of the other, by default? To know which item would do that, you need to understand z-index and stacking contexts.

Z-index #
The z-index property explicitly sets a layer order for HTML based on the 3D space of the browser—the Z axis. This is the axis which shows which layers are closer to and further from you. The vertical axis on the web is the Y axis and the horizontal axis is the X axis.

Each axis surrounding the element
The z-index property accepts a numerical value which can be a positive or negative number. Elements will appear above another element if they have a higher z-index value. If no z-index is set on your elements then the default behaviour is that document source order dictates the Z axis. This means that elements further down the document sit on top of elements that appear before them.


In normal flow, if you set a specific value for z-index and it isn't working, you need to set the element's position value to anything other than static. This is a common place where people struggle with z-index.


This isn't the case if you are in a flexbox or grid context, though, because you can modify the z-index of flex or grid items without adding position: relative.


Negative z-index #
To set an element behind another element, add a negative value for z-index.


.my-element {
	background: rgb(232 240 254 / 0.4);
}

.my-element .child {
	position: relative;
	z-index: -1;
}
As long as .my-element has the initial value for z-index of auto, the .child element will sit behind it.


Add the following CSS to .my-element, and the .child element will not sit behind it.


.my-element {
  position: relative;
  z-index: 0;
  background: rgb(232 240 254 / 0.4);
}

Because .my-element now has a position value that's not static and a z-index value that's not auto, it has created a new stacking context. This means that even if you set .child to have a z-index of -999, it would still not sit behind .my-parent.

Stacking context #
A stacking context is a group of elements that have a common parent and move up and down the z axis together.


In this example, the first parent element has a z-index of 1, so creates a new stacking context. Its child element has a z-index of 999. Next to this parent, there is another parent element with one child. The parent has a z-index of 2 and the child element also has a z-index of 2. Because both parents create a stacking context, the z-index of all children is based on that of their parent.

The z-index of elements inside of a stacking context are always relative to the parent's current order in its own stacking context.

The <html> element is a stacking context itself and nothing can ever go behind it. You can put stuff behind the <body> until you create a stacking context with it.
Creating a stacking context #
You don't need to apply z-index and position to create a new stacking context. You can create a new stacking context by adding a value for properties which create a new composite layer such as opacity, will-change and transform. You can see a full list of properties here.

To explain what a composite layer is, imagine a web page is a canvas. A browser takes your HTML and CSS and uses these to work out how big to make the canvas. It then paints the page on this canvas. If an element was to change—say, it changes position—the browser then has to go back and re-work out what to paint.

To help with performance, the browser creates new composite layers which are layered on top of the canvas. These are a bit like post-it notes: moving one around and changing it doesn't have a huge impact on the overall canvas. A new composite layer is created for elements with opacity, transform and will-change because these are very likely to change, so the browser makes sure that change is performant as possible by using the GPU to apply style adjustments.

You can also create a stacking context by adding a filter and setting backface-visibility: hidden.
Resources #
Forcing layers
Animations Guide: Force layer creation
Understanding z-index
Check your understanding
Test your knowledge of z-index
QUESTION 1
QUESTION 2
QUESTION 3

<section>
  <article>1</article>
  <article>2</article>
  <article>3</article>
  <article>4</article>
</section>
Which article is on top by default?



1

2

3

4
CHECK
PREV
017
Focus
NEXT
019
Functions
CSS has a range of inbuilt functions. In this module you will find out about some of the key functions, and how to use them.

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
