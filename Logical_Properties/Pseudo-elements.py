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
013
Pseudo-elements
A pseudo-element is like adding or targeting an extra element without having to add more HTML. They have a variety of roles and you can learn about them in this module.

On this page
::before and ::after
::first-letter
::first-line
::backdrop
::marker
::selection
::placeholder
::cue


The CSS Podcast - 014: Pseudo-elements
If you've got an article of content and you want the first letter to be a much bigger drop cap— how do you achieve that?

A couple of paragraphs of text with a blue drop cap
In CSS, you can use the ::first-letter pseudo-element to achieve this sort of design detail.


p::first-letter {
  color: blue;
  float: left;
  font-size: 2.6em;
  font-weight: bold;
  line-height: 1;
  margin-inline-end: 0.2rem;
}

A pseudo-element is like adding or targeting an extra element without having to add more HTML. This example solution, using ::first-letter, is one of many pseudo-elements. They have a range of roles, and in this lesson you're going to learn which pseudo-elements are available and how you can use them.

::before and ::after #
Both the ::before and ::after pseudo-elements create a child element inside an element only if you define a content property.


.my-element::before {
	content: "";
}

.my-element::after {
	content: "";
}
The content can be any string —even an empty one— but be mindful that anything other than an empty string will likely be announced by a screen reader. You can add an image url, which will insert an image at its original dimensions, so you won't be able to resize it. You can also insert a counter.

Key Term

You can create a named counter and then increment it, based on its position in the document flow. There's all sorts of contexts where they can be really useful, such as automatically numbering an outline.
Once a ::before or ::after element has been created, you can style it however you want with no limits. You can only insert a ::before or ::after element to an element that will accept child elements (elements with a document tree), so elements such as <img />, <video> and <input> won't work.


Gotchas

input[type="checkbox"] is an exception. It is allowed to have pseudo-element children.
::first-letter #
We met this pseudo-element at the start of the lesson. It is worth being aware that not all CSS properties can be used when targeting ::first-letter. The available properties are:

color
background properties (such as background-image)
border properties (such as border-color)
float
font properties (such as font-size and font-weight)
text properties (such as text-decoration and word-spacing)

p::first-letter {
  color: goldenrod;
  font-weight: bold;
}

You can only use :first-letter on block containers. Therefore, it won't work if you try to add it to an element that has display: inline.
::first-line #
The ::first-line pseudo-element will let you style the first line of text only if the element with ::first-line applied has a display value of block, inline-block, list-item, table-caption or table-cell.


p::first-line {
  color: goldenrod;
  font-weight: bold;
}

Like the ::first-letter pseudo-element, there's only a subset of CSS properties you can use:

color
background properties
font properties
text properties
::backdrop #
If you have an element that is presented in full screen mode, such as a <dialog> or a <video>, you can style the backdrop—the space between the element and the rest of the page—with the ::backdrop pseudo-element:


video::backdrop {
  background-color: goldenrod;
}

The ::backdrop pseudo-element is supported in all major browsers apart from Safari.

::marker #
The ::marker pseudo-element lets you style the bullet or number for a list item or the arrow of a <summary> element.


::marker {
  color: hotpink;
}

ul ::marker {
  font-size: 1.5em;
}

ol ::marker {
  font-size: 1.1em;
}

summary::marker {
  content: '\002B'' '; /* Plus symbol with space */
}

details[open] summary::marker {
  content: '\2212'' '; /* Minus symbol with space */
}
Only a small subset of CSS properties are supported for ::marker:

color
content
white-space
font properties
animation and transition properties
You can change the marker symbol, using the content property. You can use this to set a plus and minus symbol for the closed and empty states of a <summary> element, for example.


::selection #
The ::selection pseudo-element allows you to style how selected text looks.


::selection {
  background: green;
  color: white;
}

This pseudo-element can be used to style all selected text as in the above demo. It can also be used in combination with other selectors for a more specific selection style.


p:nth-of-type(2)::selection {
  background: darkblue;
  color: yellow;
}

As with other pseudo-elements, only a subset of CSS properties are allowed:

color
background-color but not background-image
text properties
::placeholder #
Browser support
57
51
79
10.1
Source
You can add a helper hint to form elements, such as <input> with a placeholder attribute. The ::placeholder pseudo-element allows you to style that text.


input::placeholder {
  color: darkcyan;
}

The ::placeholder only supports a subset of CSS rules:

color
background properties
font properties
text properties
A placeholder is not <label> and should not be used in place of a <label>. Form elements must be labelled or they will be inaccessible.
::cue #
Browser support
26
55
79
7
Source
Last in this tour of pseudo-elements is the ::cue pseudo-element. This allows you to style the WebVTT cues, which are the captions of a <video> element.

You can also pass a selector into a ::cue, which allows you to style specific elements inside a caption.


video::cue {
  color: yellow;
}

video::cue(b) {
  color: red;
}

video::cue(i) {
  color: lightpink;
}
Check your understanding
Test your knowledge of pseudo-elements
QUESTION 1
QUESTION 2
Which of the following are not pseudo-elements?



::before

::first-paragraph

::after

::marker

::pencil

:active
CHECK
PREV
012
Spacing
NEXT
014
Pseudo-classes
Pseudo-classes let you apply CSS based on state changes. This means that your design can react to user input such as an invalid email address.

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

