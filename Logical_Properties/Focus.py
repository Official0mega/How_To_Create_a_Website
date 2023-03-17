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
017
Focus
Understand the importance of focus in your web applications. You'll find out how to manage focus, and how to make sure the path through your page works for people using a mouse, and those using the keyboard to navigate.

On this page
Why is focus important?
How elements get focus
Styling focus
In summary


The CSS Podcast - 018: Focus
On your webpage, you click a link that skips the user to the main content of the website. These are often referred to as skip links, or anchor links. When that link is activated by a keyboard, using the tab and enter keys, the main content container has a focus ring around it. Why is that?


This is because the <main> has a tabindex="-1" attribute value, which means it can be programmatically focused. When the <main> is targeted—because the #main-content in the browser URL bar matches the id—it receives programmatic focus. It's tempting to remove the focus styles in these situations, but handling focus appropriately and with care helps to create a good, accessible, user experience. It can also be a great place to add some interest to interactions.

Why is focus important? #
As a web developer, it's your job to make a website accessible and inclusive to all. Creating accessible focus states with CSS is a part of this responsibility.

Focus styles assist people who use a device such as a keyboard or a switch control to navigate and interact with a website. If an element receives focus and there is no visual indication, a user may lose track of what is in focus. This can create navigation issues and result in unwanted behaviour if, say, the wrong link is followed.

Learn more about the importance of focus for accessibility in Learn Accessibility: Focus, and more information on how to manage focus in HTML in Learn HTML: Focus.
How elements get focus #
Certain elements are automatically focusable; these are elements that accept interaction and input, such as <a>, <button>, <input> and <select>. In short, all form elements, buttons and links. You can typically navigate a website's focusable elements using the tab key to move forward on the page, and shift + tab to move backward.

There is also a HTML attribute called tabindex which allows you to change the tabbing index—which is order in which elements are focused—every time someone presses their tab key, or focus is shifted with a hash change in the URL or by a JavaScript event. If tabindex on a HTML element is set to 0, it can receive focus via the tab key and it will honour the global tab index, which is defined by the document source order.

If you set tabindex to -1, it can only receive focus programmatically, which means only when a JavaScript event happens or a hash change (matching the element's id in the URL) occurs. If you set tabindex to be anything higher than 0, it will be removed from the global tab index, defined by document source order. Tabbing order will now be defined by the value of tabindex, so an element with tabindex="1" will receive focus before an element with tabindex="2", for example.

Warning

Honoring document source order is really important, and focus order should only be changed if you absolutely have to change it. This applies both when setting tabindexand changing visual order with CSS layout, such as flexbox and grid. Anything that creates unpredictable focus on the web can create an inaccessible experience for the user.
Styling focus #
The default browser behavior when an element receives focus is to present a focus ring. This focus ring varies between both browser and operating systems.


This behavior can be changed with CSS, using the :focus, :focus-within and :focus-visible pseudo-classes that you learned about in the pseudo-classes lesson. It is important to set a focus style which has contrast with the default style of an element. For example, a common approach is to utilize the outline property.


a:focus {
  outline: 2px solid slateblue;
}

The outline property could appear too close to the text of a link, but the outline-offset property can help with that, as it adds extra visual padding without affecting the geometric size that the element fills. A positive number value for outline-offset will push the outline outwards, a negative value will pull the outline inwards.


Currently in some browsers, if you have a border-radius set on your element and use outline, it won't match—the outline will have sharp corners. Due to this, it is tempting to use a box-shadow with a small blur radius because box-shadow clips to the shape, honouring border-radius, but this style will not show in Windows High Contrast Mode. This is because Windows High Contrast Mode doesn't apply shadows, and mostly ignores background images to favor the user's preferred settings.



In summary #
Creating a focus state that has contrast with an element's default state is incredibly important. The default browser styles do this already for you, but if you want to change this behaviour, remember the following:

Avoid using outline: none on an element that can receive keyboard focus.
Avoid replacing outline styles with box-shadow. as they don't show up in Windows High Contrast Mode.
Only set a positive value for tabindex on an HTML element if you absolutely have to.
Make sure the focus state is very clear vs the default state.
Check your understanding
Test your knowledge of focus
QUESTION 1
QUESTION 2
Which of the following are automatically focusable elements?



<a>

<p>

<button>

<input>

<output>

<select>
CHECK
PREV
016
Shadows
NEXT
018
Z-index and stacking contexts
In this module find out how to control the order in which things layer on top of each other, by using z-index and the stacking context.

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
