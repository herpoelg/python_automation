import nbformat

# Reading the notebooks
first_notebook = nbformat.read('1 Introduction and Optimization Problems - Knapsack.ipynb', 4)
second_notebook = nbformat.read('2 Optimization Problems - Dynamic Programming.ipynb', 4)

n3_notebook = nbformat.read('3 Graph-theoretic Models - Shortest Path.ipynb', 4)
n4_notebook = nbformat.read('4 Stochastic Thinking - Birthday Problem.ipynb', 4)
n5_notebook = nbformat.read("5 Random Walks - Drunkard's Walk.ipynb", 4)
n6_notebook = nbformat.read('6 Monte Carlo Simulation.ipynb', 4)
n7_notebook = nbformat.read('7 Confidence Intervals.ipynb', 4)
n8_notebook = nbformat.read('8 Sampling and Standard Error.ipynb', 4)
n9_notebook = nbformat.read('9 Understanding Experimental Data.ipynb', 4)
n10_notebook = nbformat.read('10 Understanding Experimental Data (cont.).ipynb', 4)
n11_notebook = nbformat.read('11 Introduction to Machine Learning.ipynb', 4)
n12_notebook = nbformat.read('12 Clustering.ipynb', 4)
n13_notebook = nbformat.read('13 Classification.ipynb', 4)
n14_notebook = nbformat.read('14 Statistical Sins I.ipynb', 4)
n15_notebook = nbformat.read('15 Statistical Sins II.ipynb', 4)






# Creating a new notebook
final_notebook = nbformat.v4.new_notebook(metadata=first_notebook.metadata)

# Concatenating the notebooks
final_notebook.cells = first_notebook.cells + second_notebook.cells + n3_notebook.cells + n4_notebook.cells + n5_notebook.cells + n6_notebook.cells + n7_notebook.cells + n8_notebook.cells + n9_notebook.cells + n10_notebook.cells + n11_notebook.cells + n12_notebook.cells + n13_notebook.cells + n14_notebook.cells + n15_notebook.cells

# Saving the new notebook
nbformat.write(final_notebook, 'final_notebook.ipynb')
