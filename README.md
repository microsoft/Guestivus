
# Guestivus: The Git client for the rest of us!

# This project is a work in progress.  Large design decisions are still being made

# Motivation
Git is a lot of things, but user friendly isn't one of them.  As the world moves to Git as a primary solution for version
control, certain sectors are in danger of being marooned on proprietary technologies which have much friendly visual clients.

Git is great if you have a Computer Science degree but almost impossible to use if you're an artist, creative or someone who needs
to interact with version control systems as part of their work but don't care about the intricacies of branches, merging or 
even command line usage.  Guestivus aims to bridge this gap by presenting a subset of Git features in an easy to use visual client. 
Git features are mapped to a more user friendly "on rails" experience.  Guestivus focuses on binary file tracking between multiple users 
and less on merging and branching.

# Target Audience
- Game Development Art and Design Teams
- CG & VFX teams
- Less technical people who need to collaborate on lockable binary files

# How Guestivus uses Git
Guestivus is not a hack and will not subvert any Git functionality.  Other more technical people can still use standard Git tools to interact with the 
same repos used by Guestivus.  What it will do is use an enforced subset of Git functionality to ensure a stable and friendly user experience.  
Guestivus utilizes Git LFS 2 file locking to ensure the stability of systems relying on large numbers of binary files edited by large numbers of people.



# Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
