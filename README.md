

    <h1>TechBot Transformers</h1>
    <p>TechBot Transformers is a Streamlit-based application designed to provide users with information and answers about transformers and prompt engineering. The application leverages various libraries such as LangChain, OpenAI, and Chroma to process and retrieve relevant data from specific web sources.</p>

    <h2>Features</h2>
    <ul>
        <li>Web scraping and document loading from specified URLs</li>
        <li>Text splitting for manageable document chunks</li>
        <li>Embeddings and vector store for efficient retrieval</li>
        <li>Integration with OpenAI's GPT-3.5 model</li>
        <li>Interactive user interface built with Streamlit</li>
        <li>Query processing and result display</li>
    </ul>

    <h2>Installation</h2>
    <p>To run the application, you need to have Python installed. Follow the steps below to set up and run TechBot Transformers.</p>
    <ol>
        <li>
            Clone the repository:
            <pre><code>git clone https://github.com/yourusername/techbot-transformers.git
cd techbot-transformers</code></pre>
        </li>
        <li>
            Create and activate a virtual environment:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
        </li>
        <li>
            Install the required packages:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Run the Streamlit app:
            <pre><code>streamlit run main.py</code></pre>
        </li>
        <li>Open your web browser and go to <a href="http://localhost:8501">http://localhost:8501</a>.</li>
        <li>Enter your OpenAI API key in the sidebar.</li>
        <li>Enter your query in the input field and click submit.</li>
    </ol>

    <h2>Code Overview</h2>
    <p>The main components of the application are as follows:</p>

    <h3>Web Scraping and Document Loading</h3>
    <p>The <code>WebBaseLoader</code> loads content from specified URLs, filtering the HTML content using BeautifulSoup.</p>

    <h3>Text Splitting</h3>
    <p>Documents are split into chunks using <code>RecursiveCharacterTextSplitter</code> to facilitate indexing and retrieval.</p>

    <h3>Embeddings and Vector Store</h3>
    <p>OpenAI embeddings are generated and stored in a Chroma vector store for efficient retrieval.</p>

    <h3>LLM and Tools Integration</h3>
    <ul>
        <li><code>ChatOpenAI</code> is used to interact with OpenAI's GPT-3.5-turbo-0125 model.</li>
        <li>A retriever tool is created using <code>create_retriever_tool</code>.</li>
        <li><code>DuckDuckGoSearchRun</code> is added for web search capabilities.</li>
        <li>An agent is created using <code>create_react_agent</code> with the LLM and tools.</li>
    </ul>

    <h3>User Interface</h3>
    <p>Streamlit is used to create an interactive UI, allowing users to input their OpenAI API key and queries.</p>

    <h3>Query Processing</h3>
    <p>The agent processes the query using the LLM and tools, and the result is displayed in the Streamlit app.</p>

    
