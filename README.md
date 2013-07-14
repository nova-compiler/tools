# Tools

Utilities for the Nova project. Requires Python 3.

TODO: include code-check lint tool.

## substitute.py

It replaces variables in a file with the corresponding value in context file. For example, given the following context file,

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
And the lord of %% will almost disappear.
</pre>

will be transformed to,

<pre>
The cake is a lie.
And the lord of % will almost disappear.
</pre>

For usage:
<pre>
python substitute.py -i &lt;input-file&gt; -o &lt;output-file&gt; [-c &lt;context-file&gt;] [-s]
</pre>

Where &lt;input-file&gt;, &lt;output-file&gt;, and &lt;context-file&gt; are the paths of the respective files. The -s argument indicates to use strict mode, in this mode all warnings are treated as errors, and if any occurs the program aborts.
