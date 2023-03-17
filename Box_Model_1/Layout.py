#include <iostream>
int main()
{

Open menu
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
008
Layout
An overview of the various layout methods you have to choose from when building a component or page layout.

On this page
Layout: a brief history
Layout: the present and future
Understanding the display property
Flexbox and Grid
Flexbox
Grid
Flow layout
Inline block
Floats
Multicolumn layout
Positioning
Wrap-up


The CSS Podcast - 009: Layout
Imagine you're working as a developer, and a designer colleague hands you a design for a brand new website. The design has all sorts of interesting layouts and compositions: two-dimensional layouts that are considerate of viewport width and height, as well as layouts that need to be fluid and flexible. How do you decide the best way to style these with CSS?

CSS provides us with various ways to solve layout problems, on a horizontal axis, vertical axis, or even both. Choosing the right layout method for a context can be hard, and often you may need more than one layout method to solve your problem. To help with this, in the following modules, you'll learn about the unique features of each CSS layout mechanism to inform those decisions.

Layout: a brief history #
In the early days of the web, designs more complex than a simple document were laid out with <table> elements. Separating HTML from visual styles was made easier when CSS was widely adopted by browsers in the late '90s. CSS opened the door to developers being able to completely change the look and feel of a website without ever touching HTML. This new capability inspired projects such as The CSS Zen Garden, which was created to demonstrate the power of CSS to encourage more developers to learn it.

CSS has evolved as our needs for web design and browser technology have evolved. You can read how CSS layout and our approach to layout has evolved over time in this article by Rachel Andrew.

A timeline showing how CSS has evolved over the years, starting in 1996 up to 2021
Layout: the present and future #
Modern CSS has exceptionally powerful layout tooling. We have dedicated systems for layout and we're going to have a high-level look at what we have at our disposal, before digging into more detail of Flexbox and Grid in the next modules.

Understanding the display property #
The display property does two things. The first thing it does is determine if the box it is applied to acts as inline or block.


.my-element {
  display: inline;
}
Inline elements behave like words in a sentence. They sit next to each other in the inline direction. Elements such as <span> and <strong>, which are typically used to style pieces of text within containing elements like a <p> (paragraph), are inline by default. They also preserve surrounding whitespace.

A diagram showing all the different sizes of a box and where each sizing section starts and ends
You can't set an explicit width and height on inline elements. Any block level margin and padding will be ignored by the surrounding elements.


.my-element {
	display: block;
}
Block elements don't sit alongside each other. They create a new line for themselves. Unless changed by other CSS code, a block element will expand to the size of the inline dimension, therefore spanning the full width in a horizontal writing mode. The margin on all sides of a block element will be respected.


.my-element {
	display: flex;
}
The display property also determines how an element's children should behave. For example, setting the display property to display: flex makes the box a block-level box, and also converts its children to flex items. This enables the flex properties that control alignment, ordering and flow.

Flexbox and Grid #
There are two main layout mechanisms that create layout rules for multiple elements, flexbox and grid. They share similarities, but are designed to solve different layout problems.

We will be going into much more detail for both of these in future modules, but here is a high-level overview of what both are and what they are useful for.
Flexbox #

.my-element {
	display: flex;
}
Flexbox is a layout mechanism for one-dimensional layouts. Layout across a single axis, either horizontally or vertically. By default, flexbox will align the element's children next to each other, in the inline direction, and stretch them in the block direction, so they're all the same height.


Items will stay on the same axis and not wrap when they run out of space. Instead they will try to squash onto the same line as each other. This behaviour can be changed using the align-items, justify-content and flex-wrap properties.


Flexbox also converts the child elements to be flex items, which means you can write rules on how they behave inside a flex container. You can change alignment, order and justification on an individual item. You can also change how it shrinks or grows using the flex property.


.my-element div {
 	flex: 1 0 auto;
}
The flex property is a shorthand for flex-grow, flex-shrink and flex-basis. You can expand the above example like this:


.my-element div {
 flex-grow: 1;
 flex-shrink: 0;
 flex-basis: auto;
}
Developers provide these low-level rules to hint a browser how the layout should behave when it is challenged by content and viewport dimensions. This makes it a very useful mechanism for responsive web design.

Grid #

.my-element {
	display: grid;
}
Grid is similar in a lot of ways to flexbox, but it is designed to control multi-axis layouts instead of single-axis layouts (vertical or horizontal space).

Grid enables you to write layout rules on an element that has display: grid, and introduces a few new primitives for layout styling, such as the repeat() and minmax() functions. One useful grid unit is the fr unit—which is a fraction of remaining space—you can build traditional 12 column grids, with a gap between each item, with 3 CSS properties:


.my-element {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1rem;
}

This example above shows a single axis layout. Where flexbox mostly treats items as a group, grid gives you precise control over their placement in two dimensions. We could define that the first item in this grid takes up 2 rows and 3 columns:


.my-element :first-child {
  grid-row: 1/3;
  grid-column: 1/4;
}
The grid-row and grid-column properties instruct the first element in the grid to span to the start of the fourth column, from the first column, then span to the third row, from the first row.


Flow layout #
If not using grid or flexbox, your elements display in normal flow. There are a number of layout methods that you can use to adjust the behavior and position of items when in normal flow.

Inline block #
Remember how surrounding elements don't respect block margin and padding on an inline element? With inline-block you can cause that to happen.


p span {
	display: inline-block;
}
Using inline-block gives you a box that has some of the characteristics of a block-level element, but still flows inline with the text.


p span {
	margin-top: 0.5rem;
}

Floats #
If you have an image that sits within a paragraph of text, wouldn't it be handy for that text to wrap around that image like you might see in a newspaper? You can do this with floats.


img {
	float: left;
	margin-right: 1em;
}
The float property instructs an element to "float" to the direction specified. The image in this example is instructed to float left, which then allows sibling elements to "wrap" around it. You can instruct an element to float left, right or inherit.


Warning

When you use float, keep in mind that any elements following the floated element may have their layout adjusted. To prevent this, you can clear the float, either by using clear: both on an element that follows your floated element or with display: flow-root on the parent of your floated elements. Find out more in the article The end of the clearfix hack.
Multicolumn layout #
If you have a really long list of elements, such as a list of all of the countries of the world, it can result in a lot of scrolling and time wasted for a user. It can also create excess whitespace on the page. With CSS multicolumn, you can split this into multiple columns to help with both of these issues.


<h1>All countries</h1>
<ul class="countries">
  <li>Argentina</li>
  <li>Aland Islands</li>
  <li>Albania</li>
  <li>Algeria</li>
  <li>American Samoa</li>
  <li>Andorra</li>
  …
</ul>

.countries {
	column-count: 2;
	column-gap: 1em;
}
This automatically splits that long list into two columns and adds a gap between the two columns.



.countries {
	width: 100%;
	column-width: 260px;
	column-gap: 1em;
}

Instead of setting the number of columns that the content is split into, you can also define a minimum desired width, using column-width. As more space is made available in the viewport, more columns will automatically be created and as space is reduced, columns will also reduce. This is very useful in responsive web design contexts.

Positioning #
Last on this overview of layout mechanisms is positioning. The position property changes how an element behaves in the normal flow of the document, and how it relates to other elements. The available options are relative, absolute, fixed and sticky with the default value being static.


.my-element {
  position: relative;
  top: 10px;
}
This element is nudged 10px down based on its current position in the document, as it is positioned relative to itself. Adding position: relative to an element also makes it the containing block of any child elements with position: absolute. This means that its child will now be repositioned to this particular element, instead of the topmost relative parent, when it has an absolute position applied to it.


.my-element {
  position: relative;
  width: 100px;
  height: 100px;
}

.another-element {
	position: absolute;
	bottom: 0;
	right: 0;
	width: 50px;
	height: 50px;
}
When you set position to absolute, it breaks the element out of the current document flow. This means two things:

You can position this element wherever you like, using top, right, bottom and left in its nearest relative parent.
All of the content surrounding an absolute element reflows to fill the remaining space left by that element.
An element with a position value of fixed behaves in a similar way to absolute, with its parent being the root <html> element. Fixed position elements stay anchored from the top left based on the top, right, bottom and left values that you set.

You can achieve the anchored, fixed aspects of fixed and the more predictable document flow-honoring aspects of relative by using sticky. With this value, as the viewport scrolls past the element, it stays anchored to the top, right, bottom and left values that you set.


Wrap-up #
There's a lot of choice and flexibility with CSS layout. To dive further into the power of CSS Flexbox and Grid, continue into the next few modules.

Check your understanding
Test your knowledge of layout
QUESTION 1
QUESTION 2
QUESTION 3
QUESTION 4
What 2 things does the display property do?



Determines inline or block or none.

Determines the grid layout frame.

Determines how the children should behave.

Determines if the box should scroll.
CHECK
PREV
007
Sizing Units
NEXT
009
Flexbox
Flexbox is a layout mechanism designed for laying out groups of items in one dimension. Learn how to use it in this module.

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
