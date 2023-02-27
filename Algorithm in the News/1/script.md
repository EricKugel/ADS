# AI Detects Lung Cancer

## Sibyls
Researchers at MIT have created an AI that can not only find lung cancer, but predict it in patients up to 6 years in advance. It's name is Sybil, and it's named after the Sibyls of greek mythology, who were female prophets.

## How it works
### Slices
The AI analyzes CT scans. CT scans take a whole bunch of cross sections of the lungs using x-rays, and together, it forms a 3D image. This is a picture of the brain, not the lungs, but the process is the same. What's tricky about CT scans is that the data is massive. Modern CT scans take anywhere from 128 to 640 slices, and trying to analyze that much image is difficult. 

### Nodules
There's also a lot of misleading data, because the lungs naturally have little dense parts called nodules, from infections or irritations, that can look cancerous.
 
### AI
So to be able to sift through all the slices, ignoring the nodules and finding the tiny, tiny little signs of cancer, the team needed a lot of training data. They manually labeled hundreds of CT scans, and eventually, the AI was able to not only identify cancer but predict it in lungs without cancer, down to which side it would be on. Even the team was surprised by it.

## Interfacing
This kind of mysterious predictive power reminds me a lot of the Sibyls, who would deliver their prophecies in riddles. It also reminds me of the concept of interfacing. Just like with data structures and programming languages, the team doesn't know how the model works, and they're not even entirely sure how it's able to see cancer in lungs they aren't able to. But yet, it definitely works, and it is extremely accurate too, at up to 94% in some tests. Similarly, programmers don't need to know the exact code that makes their dictionary map keys to values or the choices and assumptions the creator made to maximize efficiency. They just need to know how it inputs and outputs. AI is similar, but the level of abstraction is even foggier. I think it's incredible that the AI is saving lives and the research team isn't even sure how.

## World Effects
And the AI definitely has the power to save lives. The strategy before was to just screen high-risk patients or patients with symptoms in the hopes that cancer would be detected in the early stages. Sibyl can predict cancer before it starts, and the researchers hope that it will be able to widen the availability of screening. Currently, because of stigma against smokers and the lack of predictive models, screening isn't very common. However, a growing number of people with lung cancer, up to half in women, are non-smokers. Hopefully Sibyl will be the reason that lung cancer is no longer the most deadly form of cancer in the future.