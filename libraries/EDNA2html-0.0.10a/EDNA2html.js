/* EDNA2html.js

   Javascript functions for use in the output of EDNA2html

   CVS_id $Id: EDNA2html.js,v 1.3 2010/04/22 09:19:34 pjb93 Exp $

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU Lesser General Public License as published
   by the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

   You should have received a copy of the GNU General Public License
   and the GNU Lesser General Public License  along with this program.  
   If not, see <http://www.gnu.org/licenses/>.

 */

// Toggle the display property of a specific element
// Specify the id of an element and its display style
// will be flipped from "none" to "block", or "block" to
// "none" as appropriate
function toggleElement(name)
{
    var obj = document.getElementById(name);
    var state = obj.style.display;
    var new_state = "";
    if (state == "none") {
	new_state = "block";
    } else {
	new_state = "none";
    }
    obj.style.display = new_state;
}

// Toggle the display properties of multiple elements
// Specify a list of element ids to have their display
// style flipped between "none" and "block"
function toggleElements()
{
    for (var i=0; i < arguments.length; i++) {
	toggleElement(arguments[i]);
    }
}

// General function to reveal a specific element
// Specify the id of an element and its display
// style will be changed to "block"
function showElement(element_id)
{
    // This changes the display style to be "block"
    var obj = document.getElementById(element_id);
    obj.style.display = "block";
}

// General function to hide a specific element
// Specify the id of an element and its display
// style will be changed to "none"
function hideElement(element_id)
{
    // This changes the display style to be "none"
    var obj = document.getElementById(element_id);
    obj.style.display = "none";
}

// General function to set the display property for all elements
// with a specific class
function setDisplayByClass(classname,value)
{
    // Get all elements in the document
    var elements = getElementsByClass(classname);

    // For each element look for the "class" attribute
    for (var i = 0; i < elements.length; i++) {
        var node = elements[i];
	node.style.display = value;
    }
}

// General function to add a class to an element
// If the class is already associated with the element then
// nothing is done
function addClassToElement(element,classname)
{
    var classes = element.getAttribute('class');
    var attributeName = 'class';
    if (classes == null) {
	// If the attribute is null then try using the
	// 'className' attribute instead
	// This works for IE7 and IE6
	classes = element.getAttribute('className');
	attributeName = 'className';
    }
    if (classes != null) {
	classes = classes.split(" ");
	for (var k in classes) {
	    if (classes[k] == classname) {
		// Already has this class associated with it
		return
	    }
	}
    } else {
	// It's possible that there aren't any classes
	// attached to the element
	attributeName = 'class';
	classes = new Array();
    }
    // Append the new class name to the array and concatenate
    classes.push(classname);
    classes = classes.join(" ");
    // Update the classes associated with the element
    element.setAttribute(attributeName,classes);
}

// General function to remove a class from an element
// If the class isn't associated with the element then
// nothing is done
function removeClassFromElement(element,classname)
{
    var classes = element.getAttribute('class');
    var attributeName = 'class';
    if (classes == null) {
	// If the attribute is null then try using the
	// 'className' attribute instead
	// This works for IE7 and IE6
	classes = element.getAttribute('className');
	attributeName = 'className';
    }
    var new_classes = "";
    if (classes != null) {
	classes = classes.split(" ");
	for (var k in classes) {
	    if (classes[k] != classname) {
		// Keep this class
		new_classes = new_classes + " " + classes[k];
	    }
	}
    }
    element.setAttribute(attributeName,new_classes);
}

// General function to fetch and return an array of elements
// which are children of the specified element and which are
// also associated with the specified class
// This is able to deal with elements that belong to multiple
// classes
function getChildElementsByClass(element,classname)
{
    // Array of matching elements
    var matches = new Array();

    // Get all elements in the document
    var elements = element.getElementsByTagName("*");

    // For each element look for the "class" attribute
    for (var i = 0; i < elements.length; i++) {
        var node = elements.item(i);
        // First try to get the class attribute using 'class'
        // This seems to work on Firefox 2.* and 1.5
        var classes = node.getAttribute('class');
        if (classes == null) {
            // If the attribute is null then try using the
            // 'className' attribute instead
            // This works for IE7 and IE6
            classes = node.getAttribute('className');
        }
        if (classes != null) {
            classes = classes.split(" ");
            for (var k in classes) {
                if (classes[k] == classname) {
		    // Found a match
	            matches[matches.length] = node;
                }
            }
        }
    }

    // Return array of matching elements
    return matches;
}

