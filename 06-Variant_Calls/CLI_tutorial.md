Variant Calling Walkthrough with Command Line Tools on AWS EC2

This tutorial outlines how to perform variant calling using FreeBayes on a free-tier AWS EC2 instance. The steps leverage Docker containers to simplify tool setup.

⸻

1. Set Up AWS EC2 Instance

Create and Launch
	•	Create an AWS account
	•	Launch a free-tier eligible EC2 instance (Amazon Linux 2 or similar)
	•	Choose instance type: t2.micro
	•	Enable ports as needed (SSH access enabled by default)

⸻

2. Initial EC2 Setup

SSH into the instance, then run:

sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
newgrp docker

Test Docker installation:

docker run hello-world


⸻

3. Pull Required Docker Images

docker pull quay.io/biocontainers/mulled-v2-7bde9f0045905cc44cb726ad016ff10c70a194d7:868e195f26a5b9b98af841423faef4052e50d640-0

docker tag quay.io/biocontainers/mulled-v2-7bde9f0045905cc44cb726ad016ff10c70a194d7:868e195f26a5b9b98af841423faef4052e50d640-0 mulled-env

docker pull quay.io/biocontainers/snpeff:5.2--hdfd78af_1

docker tag quay.io/biocontainers/snpeff:5.2--hdfd78af_1 snpeff_env


⸻

4. Download Reference Files and Data

wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz
gunzip hg19.fa.gz

wget https://zenodo.org/records/60520/files/GIAB-Ashkenazim-Trio.txt
wget https://zenodo.org/records/60520/files/GIAB-Ashkenazim-Trio-hg19.gz


⸻

5. Index Reference and BAM Files

docker run --rm -v $(pwd):/data mulled-env samtools faidx /data/hg19.fa

docker run --rm -v $(pwd):/data mulled-env samtools index /data/GIAB-Ashkenazim-Trio-hg19.gz


⸻

6. Run FreeBayes for Variant Calling

docker run --rm -v $PWD:/data mulled-env \
  freebayes \
    --bam /data/GIAB-Ashkenazim-Trio-hg19.gz \
    --fasta-reference /data/hg19.fa \
    --vcf /data/freebayes_output.vcf \
    -B 1000 \
    -W 1,3 \
    -D 0.9 \
    --genotype-qualities \
    --genotyping-max-banddepth 6


⸻

7. Normalize Variants with vcfallelicprimitives

docker run --rm -v $PWD:/data mulled-env \
  bash -c "cat /data/freebayes_output.vcf | \
    vcfallelicprimitives \
      -t 'Split primitives' \
      -L 200 \
      --keep-info \
      --keep-geno \
    > /data/freebayes_output.primitives.vcf"


⸻

You now have a VCF file with normalized variant calls, ready for annotation or downstream analysis. All tools used are available in Docker images, and the workflow is reproducible and compatible with free-tier AWS resources.
