import sublime, sublime_plugin
import urllib2, re, sys

class HideSourceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World4!")
		window = self.view.window()
		#window.show_quick_panel(['messages'], None, sublime.MONOSPACE_FONT)
		#firstline_region = self.view.line(sublime.Region(0,1))#self.view.full_line(1)
		## DOCUMENTATION
		## - METADATA: 213
		comment_regions = self.view.find_all('^\s*##')
		all_regions =     self.view.find_all('^\s*..')
		comment_region_lines = []
		comment_region_strings = []
		full_comment_regions = []
		full_other_regions = []
		prev_region = False
		#big_region = sublime.Region(0,0)
		for x in all_regions:
			if x in comment_regions:
				full_line = self.view.full_line(x)
				if (prev_region):
					if prev_region.end() == full_line.begin():
						full_line = sublime.Region(prev_region.begin(), full_line.end())
				#print full_line
				full_comment_regions.append(full_line)
				prev_region = full_line
				full_line = sublime.Region(full_line.begin(), full_line.end()-1)
				comment_region_lines.append(full_line)
				#comment_region_strings.append(self.view.substr(self.view.line(x)))
				#big_region = big_region.cover(x)
			else:
				full_line = self.view.full_line(x)
				full_other_regions.append(full_line)
		##	DOCUMENTATION END	

		#comment_string = self.view.substr(firstline_regions)
		#window.show_quick_panel(comment_region_strings, None, sublime.MONOSPACE_FONT)
		
		if(not self.view.fold(comment_region_lines)):
			self.view.unfold(comment_region_lines)

		#if (not self.view.fold([big_region])):
	#		self.view.unfold([big_region])
		#print(self.view.size())
		#self.view.insert(edit, self.view.size(), "\nAt end?")
		#print all_regions
		bigstring = ""
		for r in full_other_regions:
			#print(self.view.substr(r))
			bigstring += self.view.substr(r)
			sys.stdout.write(self.view.substr(r))
		#self.view.insert(edit, self.view.size(), "\n\n---\n"+bigstring)
