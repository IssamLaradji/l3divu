import pandas as pd

# read l3divu.txt
df = pd.read_csv("meta.txt", sep="\t")
# Get the "Status" and "Paper ID" columns as a list
df_status = df["Status"].tolist()
df_paper_id = df["Paper ID"].tolist()

# Loop over the paper IDs and read the pdf under the folder "papers"
for i, paper_id in enumerate(df_paper_id):
    # get the status of the paper
    status = df_status[i]
    # remove space from the status
    status = status.replace(" ", "")
    # get the pdf file path which is papers/{paper_id}/Submission/*.pdf
    # where * needs to be extracted by glob
    import glob

    pdf_path = glob.glob(f"papers/{paper_id}/Submission/*.pdf")[0]

    # copy the pdf file to the folder "{status}/{paper_id}.pdf"
    import shutil, os

    # create folder if it does not exist
    if not os.path.exists(status):
        os.makedirs(status)
    shutil.copy(pdf_path, f"{status}/{paper_id}.pdf")

    # print progress bar
    print(f"{i+1}/{len(df_paper_id)}")
