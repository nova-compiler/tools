# Tools

Utilities for the Nova project. Requires Python 3.

TODO: include code-check lint tool.

## substitute.py

It substitute variables in files by a value existing in other files. For example, with a configuration file as:

<pre>
{
	"context" : {
		"thing" : "cake"
	}
}
</pre>

The template text,

<pre>
The %thing% is a lie.
</pre>

will be substituted to,

<pre>
The cake is a lie.
</pre>

For usage:
<pre>
python substitute.py -i &lt;input-file&gt; -o &lt;output-file&gt; [-c &lt;context-file&gt;]
</pre>

Where &lt;input-file&gt;, &lt;output-file&gt;, and &lt;context-file&gt; are the paths of the respective files.
