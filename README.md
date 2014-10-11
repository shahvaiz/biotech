Protein Simulation
=======
http://protein-simulation.herokuapp.com/welcome/

This is a protein application that I created in my bioinformatics class at Georgetown University. This program is able to simulate scientific behavior using a computation model.

A user inputs a protein sequence (an amino acid string comprised of the letters A, C, T, and G). The user selects an enzyme (a substance which "cleaves", or cuts a protein sequence at specific points). The result is a table of peptides which displays the resulting amino acid sequences.

#### More Details
- Classes are used to store the cleavage rules for each enzyme. The cleavage positions are stored in a list.
- A nested For-loop parses the amino acid strings, using the cleavage points, to create the resulting peptide sequences.
- The peptide information is stored in a nested array with the following structure:

	[[peptide1, length, weight, missed cleavages],
	[peptide2, length, weight, missed cleavages]…]]
- The array is displayed in a dynamic HTML table, which creates a row for each list in the peptide table
