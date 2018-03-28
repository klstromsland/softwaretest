# softwaretest

Review of 40 runs

atril 

tended to show more assertion errors per report (a lot)
object failure / type error / get page error / premature end of data segment / corrupt JPEG data / bad Huffman code / Invalid SOS parameters for sequential JPEG
some font thing failed

Reports
25787
25801
25847
25871
25952
25985
26057
26121
26150
26177
26237



okular
 
corrupt JPEG data, 22 extranious bytes before marker 0xc4

Reports
25862
25968
25977
25999
26033
26042
26084
26104
26114
26197
26207
26221
26230


Runs per file
7  HowToBuildaCareerinTech.pdf
15 Charlie_Miller_(security_researcher).pdf
15 Cracking the Coding Interview (4th edition) .pdf
3  Resume_Stromsland_Nest.pdf

Runs per app
22 Atril  11 reports
18 Okular 13 reports


Both programs alerted with "unable to open" but I could not figure out how to count these occurrences to try to get an idea of why this happens.

Sometimes nothing is reported.  I would like to track this also, but not sure how.

I would like to figure out how to gather relevant info from the stdout.

It is difficult for me to say if any of these are important bugs or if the software is not doing what it is suppose to do given the input.

Interesting though.


Larger Runs

100 runs

HowToBuildaCareerinTech.pdf 				runs: 22, okular: 16, atril: 6
Resume_Stromsland_Nest.pdf 				runs: 27, okular: 16, atril: 11
Charlie_Miller_(security_researcher).pdf 		runs: 26, okular: 13, atril: 13
Cracking the Coding Interview (4th edition) .pdf 	runs: 25, okular: 10, atril: 15

1000 runs

HowToBuildaCareerinTech.pdf 				runs: 259, okular: 139, atril: 120
Charlie_Miller_(security_researcher).pdf 		runs: 252, okular: 118, atril: 134
Cracking the Coding Interview (4th edition) .pdf 	runs: 264, okular: 139, atril: 125
Resume_Stromsland_Nest.pdf 				runs: 225, okular: 111, atril: 114

If I want to run small batches I see that I would need to adjust the fuzz factor.

I tried running to 10,000 a bit too early.  Ubuntu exited before it was finished and I had not yet implemented loop counting feature so I did not know how far I got.

I may try again not that it counts.


