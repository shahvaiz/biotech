Protein Simulation
=======
http://protein-simulation.herokuapp.com/welcome/

This is a protein application that I created in my bioinformatics class at Georgetown University. This program simulates scientific behavior using a computation model.

A user inputs a protein sequence (an amino acid string comprised of the letters A, C, T, and G). The user selects an enzyme (a substance which "cleaves", or cuts a protein sequence at specific points). The result is a table of peptides which displays the resulting amino acid sequences.

#### More Details
- Classes are used to store the cleavage rules for each enzyme. The cleavage positions (cut-points within the sequence) are stored in a list.
- The list of cut points is sent to a nested for-loop to create the peptides.
	- The outer loop iterates through the number of missed cleavages that the user selects.
	- The inner loop creates a list of peptides using the cut points that were created. The inner loop then calculates the length and weight of each peptide, and stores those values in a list.
- A nested array is used to store the peptide information with the following structure:
```
[ [peptide1, length, weight, missed cleavages], [peptide2, length, weight, missed cleavages ], … ]
```
- The array is displayed in a dynamic HTML table, which creates a row for each list in the peptide table.
- The application's accuracy has been validated by comparing the results to expasy.org's Peptide Cutter webpage (http://expasy.org/tools/peptidecutter/). The results are identical.