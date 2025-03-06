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

Would you like to try squashing some commits in your repo?
