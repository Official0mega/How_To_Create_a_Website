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
014
Pseudo-classes
Pseudo-classes let you apply CSS based on state changes. This means that your design can react to user input such as an invalid email address.

On this page
Interactive states
:hover
:active
:focus, :focus-within, and :focus-visible
:target
Historic states
:link
:visited
Form states
:disabled and :enabled
:checked and :indeterminate
:placeholder-shown
Validation states
Selecting elements by their index, order and occurrence
:first-child and :last-child
:only-child
:first-of-type and :last-of-type
:nth-child and :nth-of-type
:only-of-type
Finding empty elements
:empty
Finding and excluding multiple elements
:is()
:not()


The CSS Podcast - 015: Pseudo-classes
Say you've got an email sign up form, and you want the email form field to have a red border if it contains an invalid email address. How do you do that? You can use an :invalid CSS pseudo-class, which is one of many browser-provided pseudo-classes.


A pseudo-class lets you apply styles based on state changes and external factors. This means that your design can react to user input such as an invalid email address. These are covered in the selectors module, and this module will take you through them in more detail.

Unlike pseudo-elements, which you can learn more about in the previous module, pseudo-classes hook onto specific states that an element might be in, rather than generally style parts of that element.

Interactive states #
The following pseudo-classes apply due to an interaction a user has with your page.

:hover #
Browser support
1
1
12
2
Source
If a user has a pointing device like a mouse or trackpad, and they place it over an element, you can hook on to that state with :hover to apply styles. This is a useful way to hint that an element can be interacted with.


:active #
Browser support
1
1
12
1
Source
This state is triggered when an element is actively being interacted with— such as a click—before click is released. If a pointing device like a mouse is used, this state is when the click starts and hasn't yet been released.


:focus, :focus-within, and :focus-visible #
Browser support
1
1
12
1
Source
If an element can receive focus—like a <button>— you can react to that state with the :focus pseudo-class.


You can also react if a child element of your element receives focus with :focus-within.


Focusable elements, like buttons, will show a focus ring when they are in focus—even when clicked. In this sort of situation, a developer will apply the following CSS:


button:focus {
	outline: none;
}
This CSS removes the default browser focus ring when an element receives focus, which presents an accessibility issue for users who navigate a web page with a keyboard. If there is no focus style, they won't be able to keep track of where focus currently is when using the tab key. With :focus-visible you can present a focus style when an element receives focus via the keyboard, while also using the outline: none rule to prevent it when a pointer device interacts with it.


button:focus {
	outline: none;
}

button:focus-visible {
	outline: 1px solid black;
}

:target #
Browser support
1
1
12
1.3
Source
The :target pseudo-class selects an element that has an id matching a URL fragment. Say you have the following HTML:


<article id="content">
	…
</article>
You can attach styles to that element when the url contains #content.


#content:target {
	background: yellow;
}
This is useful for highlighting areas that might have been specifically linked to, such as the main content on a website, via a skip link.


Historic states #
:link #
Browser support
1
1
12
1
Source
The :link pseudo-class can be applied to any <a> element that has a href value that hasn't been visited yet.

:visited #
You can style a link that's already been visited by the user using the :visited pseudo-class. This is the opposite state to :link but you have fewer CSS properties to use for security reasons. You can only style color, background-color, border-color, outline-color and the color of SVG fill and stroke.


Order matters #
If you define a :visited style, it can be overridden by a link pseudo-class with at least equal specificity. Because of this, it's recommended that you use the LVHA rule for styling links with pseudo-classes in a particular order: :link, :visited, :hover, :active.


a:link {}
a:visited {}
a:hover {}
a:active {}
For security reasons, you can only change styles defined by a :link or unvisited state with the :visited pseudo-class, so making sure you define changeable styles first is important. Sticking to the LVHA rule will help with that.
Form states #
The following pseudo-classes can select form elements, in the various states that these elements might be in during interaction with them.

:disabled and :enabled #
Browser support
1
1
12
3.1
Source
If a form element, such as a <button> is disabled by the browser, you can hook on to that state with the :disabled pseudo-class. The :enabled pseudo-class is available for the opposite state, though form elements are also :enabled by default, therefore you might not find yourself reaching for this pseudo-class.


:checked and :indeterminate #
Browser support
1
1
12
3.1
Source
The :checked pseudo-class is available when a supporting form element, such as a checkbox or radio button is in a checked state.


The :checked state is a binary(true or false) state, but checkboxes do have an in-between state when they are neither checked or unchecked. This is known as the :indeterminate state.

An example of this state is when you have a "select all" control that checks all checkboxes in a group. If the user was to then uncheck one of these checkboxes, the root checkbox would no longer represent "all" being checked, so should be put into an indeterminate state.


The <progress> element also has an indeterminate state that can be styled. A common use case is to give it a striped appearance to indicate it's unknown how much more is needed.

:placeholder-shown #
Browser support
47
51
79
9
Source
If a form field has a placeholder attribute and no value, the :placeholder-shown pseudo-class can be used to attach styles to that state. As soon as there is content in the field, whether it has a placeholder or not, this state will no longer apply.

Validation states #
Browser support
10
4
12
5
Source
You can respond to HTML form validation with pseudo-classes such as :valid, :invalid and :in-range. The :valid and :invalid pseudo-classes are useful for contexts such as an email field that has a pattern that needs to be matched, for it to be a valid field. This valid value state can be shown to the user, helping them understand they can safely move to the next field.


The :in-range pseudo-class is available if an input has a min and max, such as a numeric input and the value is within those bounds.


With HTML forms, you can determine that a field is required with the required attribute. The :required pseudo-class will be available for required fields. Fields that are not required can be selected with the :optional pseudo-class.

It's not a good idea to rely solely on color to signify state changes— especially red and green—because colorblind and low-vision users can struggle to see a state change, or even miss it completely. A good idea is to use color to support state changes, along with text changes and icon changes to visually signify change
Selecting elements by their index, order and occurrence #
There is a group of pseudo-classes that select items based on where they are in the document.

:first-child and :last-child #
Browser support
4
3
12
3.1
Source
If you want to find the first or last item, you can use :first-child and :last-child. These pseudo-classes will return either the first or last element in a group of sibling elements.


:only-child #
Browser support
2
1.5
12
3.1
Source
You can also select elements that have no siblings, with the :only-child pseudo-class.


:first-of-type and :last-of-type #
Browser support
1
3.5
12
3.1
Source
You can select the :first-of-type and :last-of-type which at first, look like they do the same thing as :first-child and :last-child, but consider this HTML:


<div class="my-parent">
	<p>A paragraph</p>
	<div>A div</div>
	<div>Another div</div>
</div>
And this CSS:


.my-parent div:first-child {
	color: red;
}
No elements would be colored red because the first child is a paragraph and not a div. The :first-of-type pseudo-class is useful in this context.


.my-parent div:first-of-type {
	color: red;
}
Even though the first <div> is the second child, it is still the first of type inside the .my-parent element, so with this rule, it will be colored red.


:nth-child and :nth-of-type #
Browser support
1
3.5
12
3.1
Source
You're not limited to first and last children and types either. The :nth-child and :nth-of-type pseudo-classes allow you to specify an element that is at a certain index. The indexing in CSS selectors starts at 1.


You can pass more than an index into these pseudo-classes too. If you wanted to select all even elements, you can use :nth-child(even).


You can also create more complex selectors that find items at regularly spaced intervals, using the An+B microsyntax.


li:nth-child(3n+3) {
	background: yellow;
}
This selector selects every third item, starting at item 3. The n in this expression is the index, which starts at zero the 3 (3n) is how much you multiply that index by.

Let's say you have 7 <li> items. The first item that is selected is 3 because 3n+3 translates to (3 * 0) + 3. The next iteration would pick item 6 because n has now incremented to 1, so (3 * 1) + 3). This expression works for both :nth-child and :nth-of-type.

You can play around with this sort of selector on this nth-child tester or this quantity selector tool.

:only-of-type #
Browser support
1
3.5
12
3.1
Source
Lastly, you can find the only element of a certain type in a group of siblings with :only-of-type. This is useful if you want to select lists with only one item, or if you want to find the only bold element in a paragraph.


Finding empty elements #
It can sometimes be useful to identify completely empty elements, and there is a pseudo-class for that too.

:empty #
Browser support
1
1
12
3.1
Source
If an element has no children, the :empty pseudo-class applies to them. Children aren't just HTML elements or text nodes though: they can also be whitespace, which can be confusing when you're debugging the following HTML and wondering why it isn't working with :empty:


<div>
</div>
The reason is that there's some whitespace between the opening and closing <div>, so empty won't work.

The :empty pseudo-class can be useful if you have little control over the HTML and want to hide empty elements, such as a WYSIWYG content editor. Here, an editor has added a stray, empty paragraph.


<article class="post">
 <p>Donec ullamcorper nulla non metus auctor fringilla.</p>
 <p></p>
 <p>Curabitur blandit tempus porttitor.</p>
</article>
With :empty, you can find that and hide it.


.post :empty {
	display: none;
}

Finding and excluding multiple elements #
Some pseudo-classes help you to write more compact CSS.

:is() #
Browser support
88
78
88
14
Source
If you want to find all of the h2, li and img child elements in a .post element, you might think to write a selector list like this:


.post h2,
.post li,
.post img {
	…
}
With the :is() pseudo-class, you can write a more compact version:


.post :is(h2, li, img) {
	…
}
The :is pseudo-class is not only more compact than a selector list but it is also more forgiving. In most cases, if there's an error or unsupported selector in a selector list, the entire selector list will no longer work. If there's an error in the passed selectors in an :is pseudo-class, it will ignore the invalid selector, but use those which are valid.

:not() #
Browser support
1
1
12
3.1
Source
You can also exclude items with the :not() pseudo-class. For example, you can use it to style all links that don't have a class attribute.


a:not([class]) {
	color: blue;
}
A :not pseudo-class can also help you to improve accessibility. For example, an <img> must have an alt, even if its an empty value, so you could write a CSS rule that adds a thick red outline to invalid images:


img:not([alt]) {
	outline: 10px red;
}

Check your understanding
Test your knowledge of pseudo classes
QUESTION 1
QUESTION 2
QUESTION 3
QUESTION 4
Pseudo-classes act as if a class has been dynamically applied to an element, while pseudo-elements act on an element itself.



True

False
CHECK
PREV
013
Pseudo-elements
NEXT
015
Borders
A border provides a frame for your boxes. In this module find out how to change the size, style and color of borders using CSS.

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
