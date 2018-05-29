# table


|layers|numFilters||drop|params|batch_size|training loss|training acc|test loss|test acc|user|lr|comment|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|||||1367410|64|||||||OOM>6 e|
|||||215074|512|
|||||865906|128|
|||||**SGDNESMOM**|
|8|64||0.2|1253450|256|-|-|-|-|fabuk||1x5>5x1 imgaug interrupted|
|5,5,5,2|64||0.2|412490|256|59|79|91|73|fabuk||imgaug 1x5>5x1|
|||||**ADAM**|
|16|24||0.3->0.2|772258|256|21|92.39|87|81.3|||drop 0.3<20>0.2|
|16|24||0.2|771394|256|50|82|66|80|krishna| lr=.001 >40|1x5>5x1 imgaug|
|20|24||0|471394|128|17.4|93.96|34.5|89.34|keshaw| lr=.001 >40|1x3x1 imgaug|
|20|24||0.3|471394|128|40|85.6|64|83|krishna| lr=.001 >40|1x3x1 imgaug|
|24|24||0|1037602|128|-|-|-|-|keshaw| lr=.001 >32.0005 >40 .0001|1x5x1 imgaug|
||^|trying |increasing|lr|-|didn't|help|much|||| 
||^|trying |low|res|training|with|high|lr|-|krishna|62,78|75l,76a|
||^|trying |low|res|training|with|default|lr|-|krishna|-|-|
|6|24||0.20|129538|256|21|81.91|61|81.9|
|8|24||0.5|215074|512|68|75|326|47|krishna|
|24->4->24->1|24||0.5|865906|128|45|84|118|73|facebook|
||||**USED**|**IMGAUG**|**ONWARDS**||||
|6|24>32>64>128||0.2>0.3>0.4>0.5|948962|256|42|84.9|68|81.3|krishna|lr=1e-2|epoch 15>71.5|
|16|24>24>32>64||0.2>0.3>0.4>0.5|2073090|256|37|87|62|82|krishn|lr=1e-2|epoch 15->73, 20->80, multiple split machines .runs|
|5f__2l|24||0.2|125218|256|230|9.8|230|17|krishna|
|5f__2l|24||0.2|125218|256|0|~74|0|76|krishna|lr=1e-3<15>1e-4 30>1e-5|epoch 20->74|
|5f__2l|24||0.2|125218|256|64|77|82|74.9|krishna|lr=1e-3 30>1e-5|epoch 20->72|
|5f__2l|24||0.2|125218|256|67|76|74.6|76.7|krishna|lr=1e-3 5>.00075 15>.0005 25>.0001|epoch 15->73, 32>76|
|5f__2l|24||0.2|117010|256|67|76|84.2|74.3|fabuk|lr=1e-3 5>.00075 15>.0005 25>.0001| 1x5>5x1 17>72, 25>74|
||||**was**|**underfitting**|**so** |**increasing**|**filters** |**to**|**64**||
|5f__2l|64||0.2|412490|256|37|87|48|85.3|fabuk|lr=1e-3 25>.0001|1x5>5x1 epoch 16>79.6a-.58l, 34>84.8a-.47l|
||||tried|sgdnesmom|on|above| 10th |epoch|loss| 8.34|acc| 40|
|5,5,5,2|64||0.2|412490|256|34.7|87.9|45.9|86.2|fabuk|lr=1e-3 40>.0001|1x5>5x1 at 45th epoch|
|5,5,5,2|64||0.2|412490|320|41|85|61|82|amar|lr=.001 fixed|1x5>5x1 low res-> 2.3, 55|
|5,2,4,1|64||0.2|314826|256|73|74|89|70|fabuk||1x5>5x1 1-8, 8-50|
|6|64||0.2|1021514|256|57|79|65|79|krishna| lr=.001 >30<37.0001, >37 .001|1x7>7x1 epoch 8>55a-1.27l| |
|6|32||0.2|339754|256|48|82|59|81|krishna| lr=.001 >40|1x3>3x1|
|7|24||0.3|169618|512|40|85|49|83|keshaw| lr=.01<22>.001|38 epoch 3x3 no imgaug|
|7|16||0.3|78010|1024|7-24|was|better|-|keshaw| lr=.01|3x3 no imgaug|
|8|32||0.2|501290|256|68|75|106|69|fabuk| lr=.001 >40|1x5>5x1|


# Observation:
- .001 is the best LR for Adam at 256 batch size
- augmenting low res image is not good

|-|Test loss|Test accuracy|
|-|-|-|
|aug|2.191967127609253|0.5186|
|no aug|2.348378648757935|0.5593|