/* EDNA2html_sortable_table.js

   Javascript functions for use in creating the sortable summary
   table in EDNA2html

   CVS_id $Id: EDNA2html_sortable_table.js,v 1.17 2010/04/28 15:18:56 pjb93 Exp $

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

/*
  Template table:

  <table id="strategySummary">
  <thead>
  <tr>
  <th><a href="#" title="sort by run" onclick="return sortTable(this);">Run #</a></th>
  ...
  </tr>
  </thead>
  <tbody id="strategyData"><tbody>
  </table>

 */

// Data
//
// Add information about a successful EDNA run/strategy
function addStrategy(run,
		     ranking_resolution,
		     completeness,
		     ioversigma,
		     ioversigmaoverall,
		     multiplicity,
		     nimages,
		     exposuretime,
		     collectiontime,
		     strategy_resolution,
		     multi_sweep,
		     description,
		     tab_id) {
    strategyData[strategyData.length] = {
	run: run,
	ranking_resolution: ranking_resolution,
	completeness: completeness,
	ioversigma: ioversigma,
	ioversigmaoverall: ioversigmaoverall,
	multiplicity: multiplicity,
	nimages: nimages,
	exposuretime: exposuretime,
	collectiontime: collectiontime,
	strategy_resolution: strategy_resolution,
	multi_sweep: multi_sweep,
	description: description,
	tab_id: tab_id,
	failed: false
    };
}
// Add information about a failed EDNA run/strategy
function addFailedStrategy(run,tab_id) {
    strategyData[strategyData.length] = {
	run: run,
	tab_id: tab_id,
	failed: true
    };
}
var strategyData = new Array();

// Table data
var lastSorted = null;
var reverseSortOrder = false;
var showDescriptions = true;
var showRankingResolution = false;

// Tabbed folder
var tabbedFolderId = null;

function setTabbedFolderId(id) {
    tabbedFolderId = id;
}

// Help data
var helpData = new Object();
helpData = { run: '',
	     ranking_resolution: '',
	     completeness: '',
	     ioversigma: '',
	     ioversigmaoverall: '',
	     multiplicity: '',
	     nimages: '',
	     exposuretime: '',
	     collectiontime: '',
	     strategy_resolution: '',
	     description: '' };

// Function to associate help text with an attribute
// in the helpData object
function setHelp(attribute,help_text) {
    helpData[attribute] = help_text;
}

// Sorting function dispatcher invoked by table column links
function sortTable(link) {
    var sortColumn = link.firstChild.nodeValue;
    // Deal with last sorted column
    if (sortColumn == lastSorted) {
	reverseSortOrder = !reverseSortOrder;
    } else {
	reverseSortOrder = false;
    }
    lastSorted = sortColumn;
    // Do the sorting
    switch (sortColumn) {
    case "Run #":
	strategyData.sort(sortByRun);
	break;
    case "Ranking resolution (A)":
	strategyData.sort(sortByRankingResolution);
	break;
    case "Predicted completeness (%)":
	strategyData.sort(sortByCompleteness);
	break;
    case "Predicted I/sigma":
	strategyData.sort(sortByIOverSigma);
	break;
    case "Predicted I/sigma (overall)":
	strategyData.sort(sortByIOverSigmaOverall);
	break;
    case "Predicted multiplicity":
	strategyData.sort(sortByMultiplicity);
	break;
    case "# of images":
	strategyData.sort(sortByNumberOfImages);
	break;
    case "Total exposure time (min:sec)":
	strategyData.sort(sortByExposureTime);
	break;
    case "Total collection time (min:sec)":
	strategyData.sort(sortByCollectionTime);
	break;
    case "Maximum resolution (A)":
	strategyData.sort(sortByStrategyResolution);
	break;
    }
    // Rerender the table
    drawTable("strategyData");
    return false;
}

// Sorting functions invoked by sortTable()
function sortByRun(a,b) {
    if (!reverseSortOrder) {
	// Default: lowest run number comes first
	return a.run - b.run;
    } else {
	return b.run - a.run;
    }
}
function sortByRankingResolution(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	// Default: lowest value (=highest resolution) comes first
	return a.ranking_resolution - b.ranking_resolution;
    } else {
	return b.ranking_resolution - a.ranking_resolution;
    }
}
function sortByCompleteness(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	// Default: highest completeness comes first
	return b.completeness - a.completeness;
    } else {
	return a.completeness - b.completeness;
    }
}
function sortByIOverSigma(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	return b.ioversigma - a.ioversigma;
    } else {
	return a.ioversigma - b.ioversigma;
    }
}
function sortByIOverSigmaOverall(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	return b.ioversigmaoverall - a.ioversigmaoverall;
    } else {
	return a.ioversigmaoverall - b.ioversigmaoverall;
    }
}
function sortByMultiplicity(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	return b.multiplicity - a.multiplicity;
    } else {
	return a.multiplicity - b.multiplicity;
    }
}
function sortByNumberOfImages(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	return a.nimages - b.nimages;
    } else {
	return b.nimages - a.nimages;
    }
}
function sortByExposureTime(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (reverseSortOrder) {
	return a.exposuretime - b.exposuretime;
    } else {
	return b.exposuretime - a.exposuretime;
    }
}
function sortByCollectionTime(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (reverseSortOrder) {
	return a.collectiontime - b.collectiontime;
    } else {
	return b.collectiontime - a.collectiontime;
    }
}
function sortByStrategyResolution(a,b) {
    if (a.failed || b.failed) {
	return sortByFailure(a,b);
    }
    if (!reverseSortOrder) {
	// Default: lowest value (=highest resolution) comes first
	return a.strategy_resolution - b.strategy_resolution;
    } else {
	return b.strategy_resolution - a.strategy_resolution;
    }
}
function sortByFailure(a,b) {
    // Compare two strategies when one or both has failed
    if (a.failed && b.failed) {
	// If both failed then compare by run number
	return sortByRun(a,b);
    }
    // Return value based on which of the two runs has
    // failed - by default the failure comes last
    var cmp;
    if (a.failed) {
	cmp = 1;
    } else {
	cmp = -1;
    }
    // Flip return value if reverse sort order requested
    if (!reverseSortOrder) {
	return cmp;
    } else {
	return -cmp;
    }
}

// Convert time from seconds to minutes/seconds
//
// Given time t, return string converting it to minutes/seconds
// for display
function convertTimeToMinutes(t) {
    var mins = Math.floor(t/60);
    var secs = Math.round(t%60);
    // Edge case: check if rounding made seconds equal 60
    if (secs == 60) {
	mins++;
	secs = 0;
    }
    // Convert for display
    mins = mins.toFixed(0);
    secs = secs.toFixed(0);
    // Pad secs with leading zero if only one digit
    if (secs.length == 1) {
	secs = "0"+secs;
    }
    return mins+":"+secs;
}

// Draw table from strategyData array of objects
//
// tbody_id is the id for the tbody element
function drawTable(tbody_id) {
    var tr, td;
    var resoln, completeness, ioversigma, multiplicity, nimages,
	exposuretime, collectiontime, multi_sweep;
    var multi_sweep_marker = " *";
    var missing_marker = "!";
    tbody = document.getElementById(tbody_id);
    // Remove existing rows, if any
    clearTable(tbody);
    // Loop through strategies and add table row for each
    for (var i=0; i<strategyData.length; i++) {
	tr = tbody.insertRow(tbody.rows.length);
	if (strategyData[i].failed) {
	    // Write non-numeric placeholders for failed run values
	    resoln = missing_marker;
	    completeness = missing_marker;
	    ioversigma = missing_marker;
	    ioversigmaoverall = missing_marker;
	    multiplicity = missing_marker;
	    nimages = missing_marker;
	    exposuretime = missing_marker;
	    collectiontime = missing_marker;
	    strategy_resoln = missing_marker;
	} else {
	    // Get values (also set to correct number of decimal places)
	    resoln = strategyData[i].ranking_resolution.toFixed(2);
	    completeness = strategyData[i].completeness.toFixed(1);
	    ioversigma = strategyData[i].ioversigma.toFixed(1);
	    ioversigmaoverall = strategyData[i].ioversigmaoverall.toFixed(1);
	    multiplicity = strategyData[i].multiplicity.toFixed(1);
	    nimages = strategyData[i].nimages;
	    exposuretime = convertTimeToMinutes(strategyData[i].exposuretime);
	    collectiontime = convertTimeToMinutes(strategyData[i].collectiontime);
	    strategy_resoln = strategyData[i].strategy_resolution.toFixed(2);
	    // Add asterisk for multi-sweep strategy
	    if (strategyData[i].multi_sweep) {
		resoln = resoln+multi_sweep_marker;
		completeness = completeness+multi_sweep_marker;
		multiplicity = multiplicity+multi_sweep_marker;
		ioversigma = ioversigma+multi_sweep_marker;
		ioversigmaoverall = ioversigmaoverall+multi_sweep_marker;
		strategy_resoln = strategy_resoln+multi_sweep_marker;
	    }
	}
	// Write values to the table
	td = insertTableElement(tr,strategyData[i].run,helpData.run);
	if (showRankingResolution) {
	    // Only display ranking resolution if specified
	    td = insertTableElement(tr,resoln,helpData.ranking_resolution);
	}
	td = insertTableElement(tr,completeness,helpData.completeness);
	td = insertTableElement(tr,ioversigma,helpData.ioversigma);
	td = insertTableElement(tr,ioversigmaoverall,
				helpData.ioversigmaoverall);
	td = insertTableElement(tr,multiplicity,helpData.multiplicity);
	td = insertTableElement(tr,nimages,helpData.nimages);
	td = insertTableElement(tr,exposuretime,helpData.exposuretime);
	td = insertTableElement(tr,collectiontime,helpData.collectiontime);
	td = insertTableElement(tr,strategy_resoln,
				helpData.strategy_resolution);
	if (showDescriptions) {
	    // Only display descriptions if specified
	    td = insertTableElement(tr,strategyData[i].description,
				    helpData.description);
	}
	// Add summary_line class to the row
	addClassToElement(tr,"summary_line");
	// Make the row clickable
	makeClickableStrategyRow(tr,tabbedFolderId,strategyData[i].tab_id);
    }
}
// Insert table element
function insertTableElement(tr,data,help) {
    var td = tr.insertCell(tr.cells.length);
    td.innerHTML = data;
    td.setAttribute("title",help);
    return td;
}
// Remove existing table rows
function clearTable(tbody) {
    while (tbody.rows.length > 0) {
	tbody.deleteRow(0);
    }
}
// Make clickable row
function makeClickableStrategyRow(tr,folder,tab_id) {
    tr.onmouseover = function() {
	// Add a new class to the element that was selected
	// Style rules can then change the appearance to the
	// selected state
	addClassToElement(this,"selected_row");
    }
    tr.onmouseout = function() {
	// Remove the class from the element so that the
	// appearance reverts to the unselected state
	removeClassFromElement(this,"selected_row");
    }
    tr.onclick = function() {
	selectTab(folder,tab_id);
    }
}
// Initialise table
//
// This should be invoked on page load to set up
// the initial state of the sortable table
function initTable(tbody_id,show_descriptions,show_ranking_resolution) {
    // Initially sort on the run number
    showDescriptions = show_descriptions;
    showRankingResolution = show_ranking_resolution;
    lastSorted = "Run #";
    reverseSortOrder = false;
    strategyData.sort(sortByRun);
    // Draw the table
    drawTable(tbody_id);
}
