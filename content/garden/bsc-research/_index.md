---
title: 'A Tool for Constructing and Visualising Bidirectional Scattering Distribution Functions'
summary: "BSc dissertation: Framework, viewer and modified open-source render engine for working with light reflection models"
ShowReadingTime: false
ShowBreadCrumbs: false
ShowWordCount: false
showBacklinks: true
---

*Submitted in partial fulfillment of the requirements for the degree of B.Sc. Information Technology (Software Development) (Hons.) at The University of Malta (2018).*

I worked under the supervision of [Dr Keith Bugeja](https://www.um.edu.mt/profile/keithbugeja) and [Dr Sandro Spina](https://www.um.edu.mt/profile/sandrospina) to design and build a framework and visualiser to assist with working with light scattering models in game design and animation, and an integration to utilise the framework in an open-source physically-based renderer. 

Using Java and LWJGL, I built a framework and visual interface to construct arbitrary Bidirectional Reflectance Distribution Functions (BRDFs), a core term in the rendering equation, verifying the physical plausability of the BRDF implementations. Java-based Sunflow renderer was used to test the models' image quality and signal-to-noise ratios for various renders.

<!-- ![poster](images/bsc-poster.png) -->

links:
- [full text](https://drive.google.com/file/d/13XieNtgd5JgAe8DdlFiex3CRNSRz7o74/view)
- [shorter review paper](https://drive.google.com/file/d/1BgcfEyG7u2wSHq4qglZOuyRPd91-dNyu/view?usp=sharing)
- [sunflow renderer code](https://github.com/nickybu/sunflow)
- [BSDF viewer code](https://github.com/nickybu/bsdf_viewer)
- [BSDF framework code](https://github.com/nickybu/bsdf_framework)