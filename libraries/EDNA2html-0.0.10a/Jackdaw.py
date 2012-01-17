#     Jackdaw.py: interactive HTML document element generation
#     Copyright (C) Diamond 2010 Peter Briggs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
#
# Jackdaw.py
#
########################################################################

"""Jackdaw: classes and functions to generating interactive HTML elements.

Jackdaw provides classes and functions that supplement the programmatic
HTML document generation functionality of the Canary module.

Jackdaw enables interactive document elements (ToggleFolders, ToggleTables
and TabbedFolders) to be added to Canary.Document classes. The
interactivity is provided by the addition of Javascript code."""

__cvs_id__ = "$Id: Jackdaw.py,v 1.1 2010/04/22 09:15:18 pjb93 Exp $"
__version__ = "0.0.1"

#######################################################################
# Import modules that this module depends on
#######################################################################
import Canary

#######################################################################
# Class definitions
#######################################################################

# ToggleFolder
#
class ToggleFolder(Canary.DocElement):
    """Create a toggle-able document element

    ToggleFolder creates a document element that can be expanded
    (opened) or collapsed (closed) to show or hide the content.

    Create a ToggleFolder using e.g.

    folder = document.addContent(ToggleFolder(document))

    Use the addOpenLinkText and addCloseLinkText methods to specify
    the HTML that will be displayed as links to open and close
    the folder respectively.

    Add arbitrary content to the folder using the addContent method.
    This content will be displayed when the folder is open and hidden
    when it is closed.

    CSS classes for ToggleFolder elements:

    The folder is wrapped in a div element with CSS class 'toggle_folder'.
    The control to open the folder is wrapped in a span element with
    CSS classes 'control' and 'open_control', while the control to
    close the folder is wrapped in a span with CSS classes 'control'
    and 'close_control'."""

    def __init__(self,document):
        """Create a new ToggleFolder object

        'document' is a Canary.Document object that the folder
        will be added to.

        Note that the new ToggleFolder will not be part of the
        document until explicitly added via the addContent
        method of another document element."""
        Canary.DocElement.__init__(self,parent_doc=document)
        self.addCSSClass("toggle_folder")
        self.__contents = []
        # Default state
        self.openByDefault()
        # Default text for open/close links
        self.__open_link_text = "Open"
        self.__open_link_help_text = None
        self.__close_link_text = "Close"
        self.__close_link_help_text = None

    def id(self):
        """Return the id for this folder

        Overrides the base class 'id' method and returns the
        unique id that will be written to the id attribute of
        the folder container.

        This id can be used to make HTML links to the section
        from elsewhere, and as a CSS selector."""
        id = "folder_"+str(self.getDocId())
        return id

    def openId(self):
        """Return an id for the 'open' view of the folder"""
        return self.id()+"_open_view"

    def closedId(self):
        """Return an id for the 'closed' view of the folder"""
        return self.id()+"_closed_view"

    def addOpenLinkText(self,text,help_text=None):
        """Set the text for the link to switch to the 'open' view

        Optionally also add 'help_text' to be displayed as a
        tool-tip over the open link."""
        self.__open_link_text = str(text)
        self.__open_link_help_text = help_text

    def addCloseLinkText(self,text,help_text=None):
        """Set the text for the link to switch to the 'closed' view

        Optionally also add 'help_text' to be displayed as a
        tool-tip over the open link."""
        self.__close_link_text = str(text)
        self.__close_link_help_text = help_text

    def openByDefault(self):
        """Set the initial state to be the 'open' view"""
        self.__open_state = "block"
        self.__closed_state = "none"

    def closedByDefault(self):
        """Set the initial state to be the 'closed' view"""
        self.__open_state = "none"
        self.__closed_state = "block"

    def addContent(self,content):
        """Add arbitrary content to the folder

        This content will be displayed when the folder is showing
        the 'open' view, and hidden for the 'closed' view.

        'content' can be plain text or an object which supports
        a 'render' method which returns a string representation.

        Returns the same 'content' that is supplied as an argument."""
        self.__contents.append(content)
        return content

    def renderContent(self):
        """Generate a HTML version of the section"""
        # Construct the "open" view
        content = "<div id='"+self.openId()+"' "
        content += "style='display: "+self.__open_state+";'>\n"
        content += "<span class=\"control close_control\">"
        content += "<a href=\"javascript://\" "
        content += "onclick=\"toggleElements('"+self.openId()+"',"
        content += "'"+self.closedId()+"');\">"
        content += Canary.makeToolTip(self.__close_link_text,
                                      self.__close_link_help_text)
        content += "</a></span>\n"
        # Add the content for the open view
        for element in self.__contents:
            try:
                content += element.render()
            except AttributeError:
                # Assume there is no render method, try str instead
                content += str(element)
        content += "</div>\n"
        # Construct the "closed" view
        content += "<div id='"+self.closedId()+"' "
        content += "style='display: "+self.__closed_state+";'>\n"
        content += "<span class=\"control open_control\">"
        content += "<a href=\"javascript://\" "
        content += "onclick=\"toggleElements('"+self.openId()+"',"
        content += "'"+self.closedId()+"');\">"
        content += Canary.makeToolTip(self.__open_link_text,
                                      self.__open_link_help_text)
        content += "</a></span>\n"
        content += "</div>\n"
        # Return the HTML code
        return content

# Tabbed folder class
#
class TabbedFolder(Canary.DocElement):
    """Create a tabbed document element

    TabbedFolder creates a document element that consists of
    multiple 'panes' of content and a set of tabs. Only one pane
    is displayed at any one time, and switching between panes is
    achieved by clicking on the tabs.

    Create a TabbedFolder using e.g.

    tabs = document.addContent(TabbedFolder(document))

    Use the addTab method to add a new tab to the TabbedFolder,
    for example:

    tab = tabs.addTab('New tab')

    This returns a Tab instance which represents a tab/pane
    combination in the document. Arbitrary content can then be added
    to the tab pane using the addContent method of the Tab object.

    CSS classes for TabbedFolder elements:

    The default appearance of rendered TabbedFolder elements is
    determined by the 'tab_header' and 'tab_body' CSS classes. Styles
    attached to these classes determine how the tabs and panes will
    appear in the 'deselected' mode.

    The 'selected' appearance of the tabbed folders is
    controlled by the 'tab_header_selected' and 'tab_body_selected'
    classes.

    Typically the 'tab_body' style should include a 'display: none;'
    rule (to hide the pane from view when not selected) and the
    'tab_body_selected' style shoud include a 'display: block;' rule
    (to make it visible when it is selected)."""

    def __init__(self,document):
        """Create new TabbedFolder object

        'document' is a Canary.Document object that the folder
        will be added to.

        Note that the new ToggleFolder will not be part of the
        document until explicitly added via the addContent
        method of another document element."""
        Canary.DocElement.__init__(self,parent_doc=document)
        self.addCSSClass("tabbed_folder")
        self.__tabs = []

    def id(self):
        """Return the id for this folder

        Overrides the base class 'id' method and returns the
        unique id that will be written to the id attribute of
        the folder container.

        This id can be used to make HTML links to the section
        from elsewhere, and as a CSS selector."""
        id = "folder_"+str(self.getDocId())
        return id

    def addTab(self,title):
        """Add a new tab to the TabbedFolder

        Creates and returns a new Tab object. 'title' specifies
        the title text for the tab.

        See the Tab class for information on adding content to
        the tab pane."""
        new_tab = Tab(title,len(self.__tabs)+1,self)
        self.__tabs.append(new_tab)
        return new_tab

    def renderContent(self):
        """Generate HTML code for the TabbedFolder"""
        i = 0
        tab_frame = []
        tab_content = []
        # Build HTML for each tab and associated pane
        for tab in self.__tabs:
            # Add the tab
            i += 1
            # Tab header
            tab_header_class = "tab_header"
            if i == 1:
                # Make the first tab the one selected by default
                tab_header_class += " tab_header_selected"
            tab_header_id = self.id()+"-header-"+tab.id()
            tab_frame.append("<div class='"+tab_header_class+"' id='"+
                             tab_header_id+
                             "'>"+
                             "<a href=\"javascript://\" "+
                             "onclick=\"selectTab('"+
                             str(self.id())+"',"+tab.id()+
                             ");\">"+tab.renderTitle()+"</a>"+
                             "</div>")
            # Tab content
            tab_content_class = "tab_body"
            if i == 1:
                # Make the first tab the one selected by default
                tab_content_class += " tab_body_selected"
            tab_content_id = self.id()+"-content-"+tab.id()
            tab_content.append("<div class='"+tab_content_class+"' id='"+
                               tab_content_id+
                               "'>"+
                               tab.render()+
                               "</div>")
        html = "<div class='tabbed_folder_header'>"+ \
            "\n".join(tab_frame)+"</div>"
        html += "<div class='tabbed_folder_content'>"+ \
            "\n".join(tab_content)+"</div>"
        return html

# Tab class
#
class Tab:
    """Represents a tab/pane combination in a TabbedFolder

    The Tab class stores information about the title and
    content of a single tab/pane combination in a TabbedFolder.

    Tab objects should be instantiated via the addTab method
    of the TabbedFolder object that they are associated with."""

    def __init__(self,title,tab_id,parent_folder):
        """Create a tab for a TabbedFolder

        'title' is the title text for the tab.
        'parent_folder' is the TabbedFolder object that this
        Tab object is attached to."""
        self.__title = str(title)
        self.__help_text = None
        self.__tab_id = str(tab_id)
        self.__parent = parent_folder
        self.__contents = []

    def id(self):
        return self.__tab_id

    def addContent(self,content):
        """Add arbitrary content to the Tab

        This content will be displayed when the tab is showing
        in the 'selected' view, and hidden when a different tab
        is selected.

        'content' can be plain text or an object which supports
        a 'render' method which returns a string representation.

        Returns the same 'content' that is supplied as an argument."""
        self.__contents.append(content)
        return content

    def addHelp(self,help_text):
        """Associate tool-tip style help text with the tab

        'help_text' will appear as a tool-tip style bubble
        over the tab header when the mouse hovers over it."""
        self.__help_text = help_text
    
    def title(self):
        """Return the title for the tab"""
        return self.__title

    def renderTitle(self):
        """Return the HTML code for the tab title"""
        return Canary.makeToolTip(self.__title,self.__help_text)

    def render(self):
        """Generate HTML code for the Tab"""
        html = ""
        for content in self.__contents:
            html += content.render()
        return html

# ToggleTable
#
class ToggleTable(Canary.Table):
    """Create a table with toggle-able rows

    ToggleTable creates a Table element with rows that can be visible
    (opened) or hidden (collapsed) to show or hide the content.

    Create a ToggleTable using e.g.

    table = document.addContent(ToggleTable(parent_doc=document))

    Use the addOpenLinkText and addCloseLinkText methods to specify
    the HTML that will be displayed as links to open and close
    the folder respectively.

    Use the normal table methods to add rows, columns etc to the table.
    Specify a toggable row in the table using the setToggleRow method.

    CSS classes for ToggleTable elements:

    The folder is wrapped in a div element with CSS class 'toggle_table'.
    The control to open the folder is wrapped in a span element with
    CSS classes 'control' and 'open_control', while the control to
    close the folder is wrapped in a span with CSS classes 'control'
    and 'close_control'.

    Toggable rows have the CSS class 'toggle_row', and are also
    associated with the class 'hide_me' when collapsed."""

    def __init__(self,parent_doc):
        """Create a new ToggleTable object

        'parent_doc' is a Canary.Document object that the folder
        will be added to.

        Note that the new ToggleTable will not be part of the
        document until explicitly added via the addContent
        method of another document element."""
        Canary.Table.__init__(self,parent_doc=parent_doc)
        self.addCSSClass("toggle_table")
        # Default text for open/close links
        self.__open_link_text = "Expand table.."
        self.__open_link_help_text = None
        self.__close_link_text = "Collapse table.."
        self.__close_link_help_text = None

    def addOpenLinkText(self,text,help_text=None):
        """Set the text for the link to switch to the 'open' view

        Optionally also set tool-tip style help to 'help_text'."""
        self.__open_link_text = str(text)
        if help_text:
            self.__open_link_help_text = str(help_text)

    def addCloseLinkText(self,text,help_text=None):
        """Set the text for the link to switch to the 'closed' view

        Optionally also set tool-tip style help to 'help_text'."""
        self.__close_link_text = str(text)
        if help_text:
            self.__close_link_help_text = str(help_text)

    def setToggleRow(self,start,end=None):
        """Set one or more rows to be togglable

        'start' is the index of the first (or only) row to be made
        toggable; if supplied then end specifies the last row."""
        if not end:
            self.addClassToRow(start,"toggle_row hide_me")
        else:
            for i in range(start,end+1):
                self.addClassToRow(i,"toggle_row hide_me")

    def renderContent(self):
        """Internal: extends the parent class renderContent method"""
        content = Canary.Table.renderContent(self)
        # Add the controls
        content += "<span class='control open_control'>"
        content += "<a href=\"javascript://\" onclick=\"toggleTableShowRows('"+str(self.id())+"');\""
        if self.__open_link_help_text:
            content += " title='"+str(self.__open_link_help_text)+"'"
        content += ">"+str(self.__open_link_text)+"</a></span>\n"
        content += "<span class='control close_control' style='display: none;'><a href=\"javascript://\" onclick=\"toggleTableHideRows('"+str(self.id())+"');\""
        if self.__close_link_help_text:
            content += " title='"+str(self.__close_link_help_text)+"'"
        content += ">"+str(self.__close_link_text)+"</a></span>\n"
        return content

# Javascript link
#
class JavascriptLink:
    """Create a <a href=...>...</a> anchor for invoking Javascript

    This is a convenience class for generating HTML links for
    invoking Javascript functions."""

    def __init__(self,text,onclick_cmd,title=None):
        """Create a new JavascriptLink object

        'text' is the text that will appear in the link, 'onclick'
        is the Javascript that will be invoked when the link is
        clicked.

        Optional argument 'title' specifies text that will be inserted
        in the element's 'title' attribute, and should appear when the
        mouse hovers over the link."""
        self.__text = text
        self.__onclick = onclick_cmd
        self.__title = title

    def render(self):
        """Write the HTML code for the link"""
        html = "<a href='javascript://' onclick='"+\
               str(self.__onclick)+"'"
        if self.__title:
            html += " title='"+str(self.__title)+"'"
        html += ">"+str(self.__text)+"</a>"
        return html


