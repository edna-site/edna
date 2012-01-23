/* Tabbed folder functions
   Implements a tabbed document element where clicking on
   different tabs reveals the associated pane for that tab

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

// Select a specific tab for display
//
// folder is the id for the containing folder div
// tab_id is the unique id for the tab being selected
//
// The specified tab header is given the 'tab_header_selected'
// class, and the associated content pane is given the
// 'tab_body_selected' class.
//
// All other tabs are put into the default (deselected/hidden)
// view by removing these classes
function selectTab(folder,tab_id)
{
    // Deselect all tabs first
    deselectAllTabs(folder);
    hideAllTabbedContent(folder);
    // Select this tab
    var header = getTabHeaderElement(folder,tab_id);
    addClassToElement(header,"tab_header_selected");
    var content = getTabContentElement(folder,tab_id);
    addClassToElement(content,"tab_body_selected");

    // Hide all tabbed content panel
    //
    // This removes the 'tab_body_selected' class from
    // all tab content elements, putting them into the
    // default (hidden) view
    function hideAllTabbedContent(folder)
    {
	// Get the first element
	var i = 1;
	var element = getTabContentElement(folder,i);
	while (element != null) {
	    // Hide this element
	    removeClassFromElement(element,"tab_body_selected");
	    //element.style.display = "none";
	    // Next element
	    i++;
	    element = getTabContentElement(folder,i);
	}
	
    }
    
    // Hide all tabbed content panes
    //
    // This removes the 'tab_header_selected' class from
    // all tab header elements, putting them into the
    // default (deselected) view
    function deselectAllTabs(folder)
    {
	// Get the first element
	var i = 1;
	var element = getTabHeaderElement(folder,i);
	while (element != null) {
	    // Deselect element by removing the selected CSS class
	    removeClassFromElement(element,"tab_header_selected");
	    // Next element
	    i++;
	    element = getTabHeaderElement(folder,i);
	}
    }

    // Get the element associated with a folder tab header
    //
    // folder is the folder id, i is the id of the tab
    function getTabHeaderElement(folder,i)
    {
	var name = folder + "-header-" + i;
	return document.getElementById(name);
    }

    // Get the element associated with a folder tab content pane
    //
    // folder is the folder id, i is the id of the tab
    function getTabContentElement(folder,i)
    {
	var name = folder + "-content-" + i;
	return document.getElementById(name);
    }
}

// Select a specific tab in the folder and move to view it
//
// Wrapper for selectTab, which also moves the current document
// location to point to the tabbed folder in question.
//
// NB assumes that the tab is within the current URL
function goToTab(folder,tab_id)
{
    selectTab(folder,tab_id);
    location = "#"+folder;
}
