# sublime-merge-learning
Learning how to use Sublime merge


"Squashing" in Git refers to combining multiple commits into a single commit. This is useful for keeping your commit history clean, especially before merging branches.

### **Ways to Squash Commits**
1. **Squash During a Rebase**  
   If you have multiple commits and want to squash them into one:  
   ```sh
   git rebase -i HEAD~3
   ```
   - This opens an interactive rebase for the last **3** commits.
   - Change **pick** to **squash (s)** for the commits you want to merge.
   - Save and close the editor.
   - Edit the commit message and save.

2. **Squash During a Merge (`--squash`)**  
   If you're merging a branch but don’t want individual commit history:  
   ```sh
   git checkout main
   git merge --squash feature-branch
   git commit -m "Squashed commit from feature-branch"
   ```

### **Squashing in Sublime Merge**
1. Select the commits you want to squash (Shift+Click for multiple).
2. Right-click and choose **"Squash Selected Commits"**.
3. Edit the commit message and confirm.

Would you like to try squashing some commits in your repo? 🚀

In Git (and Sublime Merge), **discarding a hunk** means **removing uncommitted changes** from a specific part (hunk) of a file, rather than discarding the whole file.  

### **What is a Hunk?**  
A **hunk** is a block of changes in a file. If you've modified multiple lines, Git groups them into hunks when displaying diffs.  

### **How to Discard a Hunk in Sublime Merge**  
1. Open Sublime Merge and go to the **"Unstaged Files"** section.  
2. Click on the file you want to inspect.  
3. Find the **hunk** you want to discard.  
4. Click the **"Discard Hunk"** button (usually on the right side).  
5. Confirm the action.  

This will **revert only that part of the file** to its last committed state, while keeping other changes intact.  

⚠️ **Be careful! Discarding a hunk cannot be undone unless you have a backup or a stash.**  

Would you like to try it with a test file? 😊

Hello Riverpool
