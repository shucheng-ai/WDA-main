<template>
    <div>
        <Header/>
        <a-card title="Info" style="max-width: 800px;margin: 20px auto;">
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    username:
                </div>
                {{user.name}}</div>
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    usertype:
                </div>
                {{user.info.type}}</div>
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    business_type:
                </div>
                {{user.info.business_type}}</div>
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    expired:
                </div>
                {{user.info.expired}}</div>
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    level:
                </div>
                {{user.info.level}}</div>
            <div style="margin: 10px auto;">
                <div style="width: 120px;display: inline-block;">
                    limit:
                </div>
                {{user.info.limit}}</div>
        </a-card>
    </div>
</template>

<script>
    import Header from '../header';

    export default {
        name: "Info",
        components: {
            Header
        },
        mounted() {
            this.$request.get('/api/auth').then((data) => {
                let user = data.data.user;
                this.user = user
            })
        },
        data() {
            return {
                user: {}
            }
        }
    }
</script>

<style scoped>

</style>