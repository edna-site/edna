// ToggleTable functions
//
//   This program is free software: you can redistribute it and/or modify
//   it under the terms of the GNU Lesser General Public License as published
//   by the Free Software Foundation, either version 3 of the License, or
//   (at your option) any later version.
//
//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU Lesser General Public License for more details.
//
//   You should have received a copy of the GNU General Public License
//   and the GNU Lesser General Public License  along with this program.  
//   If not, see <http://www.gnu.org/licenses/>.
//
// Functions for showing and hidding "toggable" rows in a
// table.
//
// The tr elements for togglable rows should have the class
// 'toggle_row'. Showing and hiding is accomplished by removing
// or adding the class 'hide_me' to each row.
//
// Controls are also shown and hidden by manipulating the 'display'
// property of the 'style' attribute.
//
// Show the togglable rows
function toggleTableShowRows(id) {
    // Get the parent element
    var element = document.getElementById(id);
    // Show the hidden rows
    var rows = getChildElementsByClass(element,"toggle_row");
    for (k in rows) {
	var row = rows[k];
	removeClassFromElement(row,"hide_me");
    }
    // Hide the "open" control
    var open_control = getChildElementsByClass(element,"open_control");
    for (k in open_control) { 
	open_control[k].style.display = "none";
    }
    // Show the "close" control
    var close_control = getChildElementsByClass(element,"close_control");
    for (k in close_control) { 
	close_control[k].style.display = "inline";
    }
}
//
// Hide the toggable rows
function toggleTableHideRows(id) {
    // Get the parent element
    var element = document.getElementById(id);
    // Show the hidden rows
    var rows = getChildElementsByClass(element,"toggle_row");
    for (k in rows) {
	var row = rows[k];
	addClassToElement(row,"hide_me");
    }
    // Show the "open" control
    var open_control = getChildElementsByClass(element,"open_control");
    for (k in open_control) { 
	open_control[k].style.display = "inline";
    }
    // Hide the "close" control
    var close_control = getChildElementsByClass(element,"close_control");
    for (k in close_control) { 
	close_control[k].style.display = "none";
    }
}
