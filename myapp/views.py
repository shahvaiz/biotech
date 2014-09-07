from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from enzymerules import *
from django.template import loader, RequestContext

def protein(request):
	t = get_template('home.html')
	return render_to_response('home.html', context_instance=RequestContext(request))


def amino(request):
	dataform = request.POST.copy()
	MinLength = dataform['MinLength']
	MaxLength = dataform['MaxLength']
	MinWeight = dataform['MinWeight']
	MaxWeight = dataform['MaxLength']
	MissedCleavages = dataform['missedcleavages']
	enzyme = dataform['enzyme']
	ruletype = dataform['ruletype']

	enzyme = enzyme.strip()
	enzyme = enzyme.upper()
	enzyme = enzyme.split(' ')
	enzyme = ''.join(enzyme)

	Weights = {'A':89.0935, 'R':174.2017, 'N':132.1184, 'D':133.1032, 'C':121.1590,
	           'Q':146.1451, 'E':147.1299, 'G':75.0669, 'H':155.1552, 'I':131.1736,
	           'L':131.1736, 'K':146.1882, 'M':149.2124, 'F':165.1900, 'P':115.1310,
	           'S':105.0930, 'T':119.1197, 'W':204.2262, 'Y':181.1894, 'V':117.1469}

	elength = len(enzyme)

	if ruletype=='trypsin':
		case = Trypsin(enzyme)
		
	elif ruletype=='lysc':
		case = Lyscene(enzyme)
		
	elif ruletype=='gluc':
		case = Gluc(enzyme)
		
	case.rules()
		
	Cleavages = case.rules()
		
	Cleavages.insert(0,0)
	Cleavages.append(elength)

	PeptideTable = []

	M1 = int(int(MissedCleavages) + 2)
	for a in range(1,M1):
	    
	    Values = []

	    for x in range(0, len(Cleavages)-a):
	      
	        Values = []
	        peptide = enzyme[Cleavages[x]:Cleavages[x+a]]
	        PeptideLength = len(peptide)
	        PeptideWeight = 0
			
	        for aminoacid in peptide:

	            AAWeight = Weights.get(aminoacid)
	            PeptideWeight = PeptideWeight + AAWeight

	        Values.insert(0,peptide)
	        Values.insert(1,PeptideLength)
	        Values.insert(2,PeptideWeight)
	        Values.insert(3,a-1)
			
	        PeptideTable.append(Values)


	if len(dataform['MinLength'])==0:
		dataform['MinLength']=0
		
	if len(dataform['MaxLength'])==0:
		dataform['MaxLength']=100

	if len(dataform['MinWeight'])==0:
		dataform['MinWeight']=0
		
	if len(dataform['MaxWeight'])==0:
		dataform['MaxWeight']=10000

	MaxLength = int(dataform['MaxLength'])
	MinLength = int(dataform['MinLength'])
	MaxWeight = float(dataform['MaxWeight'])
	MinWeight = float(dataform['MinWeight'])

	counter = 1

	return render_to_response('output.html', {
    'MinLength': MinLength, 'MaxLength': MaxLength, 'MinWeight': MinWeight, 'MaxWeight': MaxWeight, 'MissedCleavages': MissedCleavages, 
    'ruletype': ruletype, 'enzyme': enzyme, 'PeptideTable': PeptideTable, counter: '1'}, context_instance=RequestContext(request))

