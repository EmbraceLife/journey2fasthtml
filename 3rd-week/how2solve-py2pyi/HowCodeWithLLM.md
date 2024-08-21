# How to code with Claude

The following thoughts were results of 2.5 days of using claude to fix an enhancement [issue](https://github.com/fastai/fastcore/issues/609) in fastcore. I was intended to document the entire journey of using claude solving this issue, but I got over-stressed and lost my pase in the second half of the journey. But I still have a [notebook](/how2solve/patchInside.ipynb) with first part of the journey, and owned [12_py2pyi.ipynb](/how2solve/12_py2pyi.ipynb) by extensively experiemnting every line of the code and write up a detailed commented [solution](/how2solve/12_py2pyi.ipynb#My-solution-with-claude) to the issue. I am still experimenting with solution codes to fully understanding its details...

### Make it joyful experience

The first thing I’ve realized is that programming is something I cannot avoid in my life. It’s something I’ll likely do every day. There will always be new issues to fix, new things to learn, and new problems to solve. So, it’s important to make the process as stress-free as possible, and even better, to make the experience enjoyable.

### Reduce cognitive burden

The second point is about the benefits of using large language models in programming. These models can help reduce pressure and save time, especially when learning a new library or module, like py2pyi in the fastcore library. For instance, **I can ask Claude or ChatGPT to give me a high-level overview of the module, then dive deeper into each component.** They can explain things at a high level or go into detailed nuances. This approach helps ease the burden of understanding a new module, allowing me to focus on the intricacies of the code and logic within different components.

Large language models can significantly reduce the cognitive load when getting started. This is important because I often feel intimidated by a module due to misunderstandings. Even when these models offer good coding solutions, I sometimes hesitate to read or try them because I don’t fully understand them. However, **starting with a basic understanding of what the module and its components do** makes it easier to dive deeper into the details. This is a big deal for me.

### Solve issues as a valuable exercise

Another important point is to view fixing issues as a joyful and valuable exercise. It’s not just about learning the module or library, but also about putting that knowledge into practice. By exploring new edges and uncharted territories through problem-solving, you can gain practical experience and deepen your understanding. This is a challenging yet motivating process, and it can turn into a rewarding and enjoyable learning experience.

### Make the source your own

The fourth point involves learning a library module through notebooks, particularly those provided by the answer.ai teams. These notebooks contain source code, tests, and a step-by-step progression towards the final code, making them excellent learning resources. **By studying each cell of the notebook and even adding your own experiments**, you can truly make the source code your own. You inject your own understanding, experimentation, and personal touch into the process. This not only enhances your grasp of the library but also feels like an achievement in itself.

### Enjoy the process of troubleshooting

Another crucial point is to approach obstacles, errors, and issues with a sense of joy rather than frustration. If the process feels painful or overly stressful, there’s a tendency to rush toward a solution. However, rushing can lead to incomplete or imperfect answers, especially when working with Claude or ChatGPT. These large language models might provide a quick solution, but without careful consideration, you may miss understanding what's wrong with the solution or the underlying issue.

To avoid this, **take your time and enjoy the process of troubleshooting. When interacting with large language models, it's essential to provide full and detailed context about the problem.** This means pasting the entire error message instead of just the final line. Once you've done that, **read the response carefully. You can also ask the model to explain how it understands the error message, how it identified the problem, and what clues led it to the conclusion.** Expanding the conversation in this way can provide deeper insights and lead to a more thorough understanding of the problem.

### Talk your problem into the thinnest pieces ✨✨✨✨✨

Another important point to note is that when I encounter a problem, it often contains multiple smaller issues, even though it presents itself as a single problem. For instance, a single issue might actually consist of four or five smaller areas that need to be fixed. If I present the entire problem to Claude or ChatGPT at once, the model might try to solve all these small issues together. This can be problematic because the solutions for different issues might conflict with each other.

A better approach is to have a thoughtful and enjoyable conversation with the model.

When we encounter a problem and seek help from large language models, **it’s essential to break the problem down into its smallest components and present each piece to the LLM, asking it to solve them one by one.** Complex problems can be difficult to manage, and our initial approach to breaking them down might not be optimal. Therefore, **it’s a good idea to discuss our approach with the LLM, asking for feedback on how we’ve dissected the problem and whether there’s a more effective way to break it down into smaller, manageable parts.**

We should avoid asking the LLM to solve a large, complex problem all at once, especially since such problems often involve multiple, intertwined components that may even conflict with each other. Requesting a single, comprehensive solution could lead to a result with internal contradictions, causing the solution to fail. Therefore, **it’s always better to decompose any problem into the smallest possible parts and tackle each part individually.**

### LLM as a blind person's cane ✨✨✨✨✨

Another very important point I want to emphasize is how to make the experience of programming and learning source code more enjoyable. I’ve realized that my old approach—sitting in a chair with my laptop, typing and experimenting with every line of code to figure out its meaning and explore its edges is hands-on and practical, but it’s also stressful. It strains my eyes and mind. I prefer to talk and listen as my way of learning, which is why I’m now leaning on large language models to assist me.

So, how can we make learning programming or a new library like FastHTML or FastCore more joyful with ChatGPT or Claude? I believe the key is not to rely on these models for direct solutions to coding problems or learning goals. Instead, **we should use them like a blind person uses a cane to navigate.** Large language models should be seen as tools that guide us step by step, rather than providing us with the exact route to our destination.

Consider this analogy: if we want to reach a distant destination on a map, we shouldn’t ask the LLM to give us the exact route because we don’t even know what the map looks like or what obstacles we’ll encounter. These obstacles could be deserts, mountains, valleys, rivers, or oceans—each requiring different tools to overcome. **We need to learn these tools as we go, rather than expecting the LLM to hand us the perfect path.** If we were simply given the route, we wouldn’t learn anything, and the process would lose its value.

Moreover, if the problems we’re tackling are complex, innovative, or rare, there might not be enough training data for ChatGPT or Claude to solve them effectively. In such cases, these models may not provide reliable answers. On the other hand, for more common and simpler problems, the models might offer accurate solutions quickly. However, receiving the solution right away deprives us of the learning experience.

**The right way to use large language models is not just to ask for answers but to use them as investigative tools. Like a blind person with a cane, we should explore what’s ahead one step at a time, make decisions, and plan our next move.** Over time, as we become more familiar with the terrain, we might be able to plan several steps ahead and choose the best tools for the challenges we face.

Large language models are excellent tools for this approach because they have a vast memory of basic toolsets, documentation, and libraries. They understand how these elements work and can answer questions about them with ease. This is exactly what we need as we navigate through learning new things. **By having conversations with the model, we can gather what we need, reason through the challenges step by step, and adjust our plan of attack as we go.** This approach is much less stressful, allowing us to stay in control of our learning process, make decisions, and truly learn as we progress. In this way, large language models become invaluable partners in our journey to mastering programming, libraries, source code, and problem-solving.

### LLM as a code interpreter ✨✨✨✨✨

This new approach to learning programming and exploring new libraries is truly fascinating. It’s definitely more enjoyable because I no longer need to sit down with a laptop, typing continuously and straining my eyes and brain. The whole process becomes much more joyful. However, my concern is that I might miss out on the hands-on experience of experimenting with code—running it line by line, exploring different possibilities, adjusting parameters, and understanding the nuances of functions and classes.

To address this, **I experimented with ChatGPT, particularly with its advanced code interpreter. I found that it almost allows me to talk to it, have it code for me, and run the program in the background.** This way, I don’t need to type or even use a computer; I can simply use my phone to communicate with it. **It can write functions, create classes, and execute code in the background, showing me the results.** While it’s not there yet, I believe that in the near future, this will become fully possible.

Given this, what I need to focus on now is using Claude and ChatGPT as companions—like a blind person’s cane. **I should use them as investigative tools to help me explore the immediate challenges, pick up the necessary techniques and skills, and understand how to apply them.** The idea is to make decisions myself and **discuss those decisions and plans with ChatGPT and Claude to refine and improve them, rather than letting the models make all the decisions for me.** By taking this step-by-step, progressive approach, I believe I can make better progress, learn more effectively, and enjoy the process more while keeping it manageable.

**Before the code interpreter is truly ready, let LLM generate detailed code snippets and explanations, and then I can run them in my local environment.** This way, I can still enjoy the hands-on experience of coding while benefiting from the guidance and support of large language models. 

### Spotting the right piece requires understanding and experimentation ✨✨✨✨✨

Another important thing to note is that when I ask detailed questions, including error messages and what I suspect went wrong, and I want ChatGPT or Claude to explore and find the solution while explaining why and how the error occurred, the models can provide detailed answers. But often, the fully polished code block provided in the response won't fix the problem right away, even though it contains the correct elements to fix.

Even though the correct elements are present in the response, **you still need to understand the situation, experiment, and carefully choose the right pieces to integrate into your codebase.** Only then do things work as expected. So, even with the right context, large language models might not give you the exact solution you need in a ready-to-use form. Your understanding remains crucial— **the better your grasp of the problem, the more understanding you have with all the tools in dealing with the problem, the more effectively you can utilize the power of large language models to get problems fixed.**

### LLM as a blind man's cane: How

Another point worth noting is the significant benefit of using large language models to help me understand each line of source code. Often, source code may involve a library that is unfamiliar to me. **In such cases, I can simply ask ChatGPT to provide a high-level overview of what that library or module does.** When the source code uses specific functions, classes, or methods from that unfamiliar library, **I can further ask for a high-level explanation of their purpose, how to use them, and why they are used in that particular context.**

Additionally, **I can ask ChatGPT to explain the source code line by line or to add detailed comments to each line of a specific function or class.** This approach not only provides a high-level understanding but also offers a detailed grasp of each line’s purpose.

In Jeremy’s notebooks, where all the source code, tests, and progressive work are documented together, this is already a great resource. However, **I can take it a step further with ChatGPT or Claude. After studying a particular function or class in the source code, I can ask the large language model to generate examples using different parameters and scenarios to test the boundaries of the use cases.**

