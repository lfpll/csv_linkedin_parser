commit 027d37b57dfa0f75bc69077db4cfb0d4372f650c
Author: Luiz Fernando Lobo <luizfernandolobo@localhost.localdomain>
Date:   Thu Dec 13 18:28:49 2018 -0200

    Parsing jobs init

diff --git a/bots_parser/general.py b/bots_parser/general.py
new file mode 100644
index 0000000..9851e57
--- /dev/null
+++ b/bots_parser/general.py
@@ -0,0 +1,26 @@
+from random import random
+
+# Return button by filter function
+def filter_tag_by_text(element,text,element_name,notSingle=True):
+	tag_list = element.find_elements_by_css_selector(element_name)
+	tag_list 	= list(filter(lambda single_elem: single_elem.text.find(text) >-1,tag_list))
+	if notSingle:
+		return tag_list
+	if len(tag_list) == 0:
+		return tag_list
+	else:
+		raise(Exception('Nothing found'))
+
+
+# Scroll all the way to the bottom of the page
+## Loads all the data of dynamical rendered pages
+def scroll_all_page(driver):
+
+	def scroll_recursive(x = 0,last_height = driver.execute_script("return document.body.scrollHeight")):
+		if x >= last_height:
+			return
+		else:
+			driver.execute_script("window.scrollTo(0, "+str(x)+");")
+			scroll_recursive(x=x+100*random(),last_height=driver.execute_script("return document.body.scrollHeight"))
+
+	scroll_recursive()
\ No newline at end of file
