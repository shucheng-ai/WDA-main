<template>
    <div class="pdf">
        <Header type="pdf"/>
        <div class="pdf-outer">

            <div class="content" style="max-width: 1200px;margin: auto">
                <a-spin tip="Loading..." v-if="loading" style="width: 100%;padding-top: 50px">
                    <div class="spin-content" style="text-align: center;margin-top: 30px">
                        正在加载文档...
                    </div>
                </a-spin>
                <div v-else style="margin-top: -50px">
                    <pdf v-for="i in numPages" :key="i" :page="i" :src="url"></pdf>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import Header from '../header'
    import pdf from 'vue-pdf'

    export default {
        components: {
            pdf,
            Header,
        },
        data() {
            return {
                pdf_name: '',
                current: ['1'],
                showKey: 1,
                tabPosition: 'top',
                url: '',
                numPages: [],
                loading: true,
            }
        },
        mounted() {
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const pdf_name = urlParams.get('pdf_name')
            this.pdf_name = pdf_name;

            let task = pdf.createLoadingTask(
                `/api/pdf?pdf_name=${pdf_name}`,
            )
            this.url = task;
            task.promise.then(
                (pdf) => {
                    this.numPages = pdf.numPages;
                    this.loading = false;
                }
            )
        },
        methods: {
            handleClick(e) {
                this.showKey = +e.key
            },
        },
    }
</script>
<style lang="less" scoped>
    .pdf {
        background: #ffffff;

        .pdf-outer {
            background: #ffffff;
            height: calc(~'100vh - 65px');
            display: flex;

            .nav {
                width: 250px;
            }

            .content {
                height: calc(~'100vh - 65px');
                overflow: scroll;
                flex: 1;
                background: #ffffff;
            }
        }
    }
</style>
