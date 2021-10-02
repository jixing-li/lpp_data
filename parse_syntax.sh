# tree parsing
cd /Applications/stanford-parser-full/stanford-parser
java -Xmx10g edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "penn" models/lexparser/englishPCFG.ser.gz /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/en/preprocess/lpp_en_snt_nopunct.csv > /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/en/preprocess/lpp_en_tree.csv
java -Xmx10g edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" models/lexparser/xinhuaFactored.ser.gz /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/cn/preprocess/lpp_cn_snt_nopunct.csv > /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/cn/preprocess/lpp_cn_tree.csv
java -Xmx10g edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" models/lexparser/frenchFactored.ser.gz /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess/lpp_fr_snt_nopunct.csv > /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess/lpp_fr_tree.csv

# clean tree
cd /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess
awk '{sub(/^[ \t]+/, ""); print}' lpp_fr_tree.csv > tmp
# in text editor: delete (PUNT .); delete (ROOT; replace (SENT to (S; replace \n)) to ); replace \n( to [sapce](
awk '$1!="" {print}' tmp > lpp_fr_tree.csv

# dependency parsing
# en & cn
cd /Applications/stanford-parser-full/stanford-parser
java -Xmx10g edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "typedDependencies" models/lexparser/englishPCFG.ser.gz /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/en/preprocess/lpp_en_snt_nopunct.csv > /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/en/preprocess/lpp_en_dependencies.csv
java -Xmx10g edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" models/lexparser/xinhuaFactored.ser.gz /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/cn/preprocess/lpp_cn_snt_nopunct.csv > /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/cn/preprocess/lpp_cn_dependencies.csv
# fr
export CLASSPATH=$CLASSPATH:/Applications/stanford-corenlp/*:
cd /Applications/stanford-corenlp
java -Xmx5g edu.stanford.nlp.pipeline.StanfordCoreNLP -props french -outputFormat text -file /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess/lpp_fr_snt_nopunct.csv -outputDirectory /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess

# clean dependency
# en & cn
cd /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/cn/preprocess
awk -v FS="(" '{print $1}' lpp_cn_dependencies.txt > tmp1
awk -v FS="," '{print $2}' lpp_cn_dependencies.txt | awk -v FS="-" '{print $1}' > tmp2
paste -d " " tmp1 tmp2 | awk '$2!="." {print;next}' > lpp_cn_dependencies_clean.csv
rm tmp*
# fr
cd /Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/fr/preprocess
awk -v RS="\n\n" '$1=="Dependency" {print $0}' lpp_fr_snt_nopunct.csv.out | sed 's/Dependency Parse (enhanced plus plus dependencies)://g' > tmp
awk '$1!~/root/ {print}' tmp > lpp_fr_dependencies.csv